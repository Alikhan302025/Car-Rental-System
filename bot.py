import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from app.handlers.start import router as start_router
from app.handlers.cars import router as cars_router
from app.handlers.rental import router as rental_router


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(cars_router)
dp.include_router(rental_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())