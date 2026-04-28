from aiogram import Router, types
from app.services.car_service import get_available_cars

router = Router()


@router.message(lambda message: message.text == "Available cars")
async def show_cars(message: types.Message):
    print("BUTTON WORKS: Available cars clicked")

    cars = await get_available_cars()
    print("CARS FROM DB:", cars)

    if not cars:
        await message.answer("No available cars right now.")
        return

    text = "Available cars:\n\n"

    for car in cars:
        text += (
            f"ID: {car['car_id']}\n"
            f"{car['brand']} {car['model']} ({car['year']})\n"
            f"Price: {car['daily_price']} ₸ / day\n"
            f"Branch: {car['city']}, {car['address']}\n\n"
        )

    await message.answer(text)