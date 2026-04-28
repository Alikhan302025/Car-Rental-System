from aiogram import Router, types
from app.services.car_service import get_available_cars

router = Router()

@router.message(lambda msg: msg.text == "Available cars")
async def show_cars(message: types.Message):
    cars = await get_available_cars()

    if not cars:
        await message.answer("No available cars")
        return
    text = "Available cars:\n\n"

    for car in cars:
        text += f"{car['brand']} {car['model']} - {car['price_per_day']}$\n"
    await message.answer(text)
