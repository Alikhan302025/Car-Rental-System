import asyncpg

async def connect_db():
    return await asyncpg.connect(
        user = "postgres",
        password = "1234",
        database = "car_rental",
        host = "localhost"
    )