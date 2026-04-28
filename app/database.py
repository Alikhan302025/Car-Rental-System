import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

async def connect_db():
    try:
        return await asyncpg.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 5432)),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            ssl="require"
        )
    except Exception as e:
        print("DB ERROR:", e)
        return None