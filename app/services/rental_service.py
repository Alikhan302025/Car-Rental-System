from app.database import connect_db
from app.services.customer_service import get_or_create_customer


async def get_user_rentals(telegram_id: int):
    """
    Returns all rentals of a Telegram user.
    """
    conn = await connect_db()

    if conn is None:
        return []

    try:
        rentals = await conn.fetch(
            """
            SELECT
                r.rental_id,
                r.start_date,
                r.end_date,
                r.status,
                c.brand,
                c.model,
                c.year,
                c.daily_price
            FROM rentals r
            JOIN customers cu ON r.customer_id = cu.customer_id
            JOIN cars c ON r.car_id = c.car_id
            WHERE cu.telegram_id = $1
            ORDER BY r.rental_id DESC;
            """,
            telegram_id
        )

        return rentals

    except Exception as e:
        print("Rental service error:", e)
        return []

    finally:
        await conn.close()


async def create_rental(user, car_id: int, start_date, end_date):
    """
    Creates a new rental for a Telegram user.
    """
    conn = await connect_db()

    if conn is None:
        return False, "Database connection error."

    try:
        customer_id = await get_or_create_customer(user)

        if customer_id is None:
            return False, "Could not find or create customer."

        car = await conn.fetchrow(
            """
            SELECT car_id, brand, model, year, daily_price
            FROM cars
            WHERE car_id = $1;
            """,
            car_id
        )

        if not car:
            return False, "Car with this ID was not found."

        active_rental = await conn.fetchrow(
            """
            SELECT rental_id
            FROM rentals
            WHERE car_id = $1 AND status = 'active';
            """,
            car_id
        )

        if active_rental:
            return False, "This car is already rented."

        days = (end_date - start_date).days

        if days <= 0:
            return False, "End date must be later than start date."

        rental = await conn.fetchrow(
            """
            INSERT INTO rentals (
                customer_id,
                car_id,
                start_date,
                end_date,
                status
            )
            VALUES ($1, $2, $3, $4, 'active')
            RETURNING rental_id;
            """,
            customer_id,
            car_id,
            start_date,
            end_date
        )

        total_price = days * car["daily_price"]

        message = (
            "✅ Rental created successfully!\n\n"
            f"Rental ID: {rental['rental_id']}\n"
            f"Car: {car['brand']} {car['model']} ({car['year']})\n"
            f"Start date: {start_date}\n"
            f"End date: {end_date}\n"
            f"Days: {days}\n"
            f"Total price: {total_price} KZT"
        )

        return True, message

    except Exception as e:
        print("Create rental error:", e)
        return False, "❌ Error while creating rental."
async def return_rental(telegram_id: int, rental_id: int):
    """
    Completes an active rental of a Telegram user.
    """
    conn = await connect_db()

    if conn is None:
        return False, "Database connection error."

    try:
        rental = await conn.fetchrow(
            """
            SELECT
                r.rental_id,
                r.status,
                c.brand,
                c.model
            FROM rentals r
            JOIN customers cu ON r.customer_id = cu.customer_id
            JOIN cars c ON r.car_id = c.car_id
            WHERE r.rental_id = $1
            AND cu.telegram_id = $2;
            """,
            rental_id,
            telegram_id
        )

        if not rental:
            return False, "Rental with this ID was not found in your rentals."

        if rental["status"] != "active":
            return False, "This rental is already completed."

        await conn.execute(
            """
            UPDATE rentals
            SET status = 'completed',
                end_date = CURRENT_DATE
            WHERE rental_id = $1;
            """,
            rental_id
        )

        message = (
            "✅ Car returned successfully!\n\n"
            f"Rental ID: {rental['rental_id']}\n"
            f"Car: {rental['brand']} {rental['model']}\n"
            "Status: completed"
        )

        return True, message

    except Exception as e:
        print("Return rental error:", e)
        return False, "❌ Error while returning the car."
async def create_damage_report(telegram_id: int, rental_id: int, description: str):
    """
    Creates a damage report for a rental that belongs to the Telegram user.
    """
    conn = await connect_db()

    if conn is None:
        return False, "Database connection error."

    try:
        rental = await conn.fetchrow(
            """
            SELECT
                r.rental_id,
                c.brand,
                c.model
            FROM rentals r
            JOIN customers cu ON r.customer_id = cu.customer_id
            JOIN cars c ON r.car_id = c.car_id
            WHERE r.rental_id = $1
            AND cu.telegram_id = $2;
            """,
            rental_id,
            telegram_id
        )

        if not rental:
            return False, "❌ Rental with this ID was not found in your rentals."

        report = await conn.fetchrow(
            """
            INSERT INTO damage_reports (
                rental_id,
                description,
                repair_cost,
                report_date
            )
            VALUES ($1, $2, 0, CURRENT_DATE)
            RETURNING report_id;
            """,
            rental_id,
            description
        )

        message = (
            "✅ Damage report created successfully!\n\n"
            f"Report ID: {report['report_id']}\n"
            f"Rental ID: {rental['rental_id']}\n"
            f"Car: {rental['brand']} {rental['model']}\n"
            f"Description: {description}\n"
            "Repair cost: 0 KZT"
        )

        return True, message

    except Exception as e:
        print("Create damage report error:", e)
        return False, "❌ Error while creating damage report."

    finally:
        await conn.close()
   