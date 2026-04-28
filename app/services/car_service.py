from app.database import connect_db
async def get_available_cars():
    conn =  await connect_db()
    rows = await conn.fetch("SELECT * FROM cars WHERE status = 'available'")
    await conn.close()
    return rows

