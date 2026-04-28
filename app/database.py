import asyncpg
from config import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT

async def connect_db():
    try:
        return await asyncpg.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            host=DB_HOST,
            port=DB_PORT
        )
    except Exception as e:
        print("Database connection error:", e)
        return None