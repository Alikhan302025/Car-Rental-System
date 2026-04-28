from app.database import connect_db


async def get_available_cars():
    conn = await connect_db()

    if conn is None:
        return []

    try:
        cars = await conn.fetch("""
            SELECT 
                c.car_id,
                c.brand,
                c.model,
                c.year,
                c.daily_price,
                b.city,
                b.address
            FROM cars c
            LEFT JOIN branches b ON c.branch_id = b.branches_id
            WHERE c.car_id NOT IN (
                SELECT car_id
                FROM rentals
                WHERE status = 'active'
            )
            ORDER BY c.car_id;
        """)
        return cars

    except Exception as e:
        print("Car service error:", e)
        return []

    finally:
        await conn.close()