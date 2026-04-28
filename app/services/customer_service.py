from app.database import connect_db


async def get_or_create_customer(user):
    """
    Gets customer by Telegram ID.
    If customer does not exist, creates a new customer.
    """
    conn = await connect_db()

    if conn is None:
        return None

    try:
        telegram_id = user.id
        first_name = user.first_name or "Unknown"
        last_name = user.last_name or ""

        customer = await conn.fetchrow(
            """
            SELECT customer_id
            FROM customers
            WHERE telegram_id = $1;
            """,
            telegram_id
        )

        if customer:
            return customer["customer_id"]

        new_customer = await conn.fetchrow(
            """
            INSERT INTO customers (
                first_name,
                last_name,
                created_at,
                telegram_id
            )
            VALUES ($1, $2, CURRENT_DATE, $3)
            RETURNING customer_id;
            """,
            first_name,
            last_name,
            telegram_id
        )

        return new_customer["customer_id"]

    except Exception as e:
        print("Customer service error:", e)
        return None

    finally:
        await conn.close()