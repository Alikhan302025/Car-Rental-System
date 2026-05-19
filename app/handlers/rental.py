from datetime import datetime
from app.services.log_service import write_log

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.services.rental_service import (
    get_user_rentals,
    create_rental,
    return_rental,
    create_damage_report
)

router = Router()


class RentCarStates(StatesGroup):
    waiting_for_car_id = State()
    waiting_for_start_date = State()
    waiting_for_end_date = State()
    waiting_for_return_rental_id = State()
    waiting_for_damage_rental_id = State()
    waiting_for_damage_description = State()


@router.message(F.text == "ℹ️ Help")
async def help_handler(message: Message):
    await message.answer(
    "🚘 Welcome to KazAvto Rental Bot!\n\n"
    "🚗 Available cars - shows cars that are free now.\n"
    "📅 Rent car - allows you to rent a car by car ID.\n"
    "📋 My rentals - shows your active and completed rentals.\n"
    "🔁 Return car - allows you to return a rented car.\n"
    "🛠 Report damage - allows you to report car damage.\n"
    "ℹ️ Help - shows this instruction."
)


@router.message(F.text == "📋 My rentals")
async def my_rentals_handler(message: Message):
    rentals = await get_user_rentals(message.from_user.id)  

    if not rentals:
        await message.answer(
            "You do not have any rentals yet.\n\n"
            "Use 'Available cars' to see available cars.\n"
            "Then use 'Rent car' to create a rental."
        )
        return

    text = "Your rentals:\n\n"

    for rental in rentals:
        text += (
            f"Rental ID: {rental['rental_id']}\n"
            f"Car: {rental['brand']} {rental['model']} ({rental['year']})\n"
            f"Start date: {rental['start_date']}\n"
            f"End date: {rental['end_date']}\n"
            f"Status: {rental['status']}\n"
            f"Daily price: {rental['daily_price']} KZT\n"
            "----------------------\n"
        )

    await message.answer(text)

@router.message(F.text == "📅 Rent car")
async def rent_car_start(message: Message, state: FSMContext):
    await message.answer(
        "Please enter the car ID you want to rent.\n\n"
        "You can check car IDs by clicking 'Available cars'."
    )

    await state.set_state(RentCarStates.waiting_for_car_id)


@router.message(RentCarStates.waiting_for_car_id)
async def rent_car_get_id(message: Message, state: FSMContext):
    try:
        car_id = int(message.text)
    except ValueError:
        await message.answer("Please enter a valid car ID as a number.")
        return

    await state.update_data(car_id=car_id)

    await message.answer(
        "Enter start date in this format:\n"
        "YYYY-MM-DD\n\n"
        "Example: 2026-05-01"
    )

    await state.set_state(RentCarStates.waiting_for_start_date)


@router.message(RentCarStates.waiting_for_start_date)
async def rent_car_get_start_date(message: Message, state: FSMContext):
    try:
        start_date = datetime.strptime(message.text, "%Y-%m-%d").date()
    except ValueError:
        await message.answer("Invalid date format. Please use YYYY-MM-DD.")
        return

    await state.update_data(start_date=start_date.isoformat())

    await message.answer(
        "Enter end date in this format:\n"
        "YYYY-MM-DD\n\n"
        "Example: 2026-05-03"
    )

    await state.set_state(RentCarStates.waiting_for_end_date)


@router.message(RentCarStates.waiting_for_end_date)
async def rent_car_get_end_date(message: Message, state: FSMContext):
    try:
        end_date = datetime.strptime(message.text, "%Y-%m-%d").date()
    except ValueError:
        await message.answer("Invalid date format. Please use YYYY-MM-DD.")
        return

    data = await state.get_data()

    car_id = data["car_id"]
    start_date = datetime.strptime(data["start_date"], "%Y-%m-%d").date()

    success, result_message = await create_rental(
        user=message.from_user,
        car_id=car_id,
        start_date=start_date,
        end_date=end_date
    )

    await message.answer(result_message)

    write_log(
    action="create_rental",
    telegram_id=message.from_user.id,
    details=result_message
)

    await state.clear()


@router.message(F.text == "🔁 Return car")
async def return_car_handler(message: Message, state: FSMContext):
    await message.answer(
        "Please enter the Rental ID you want to return.\n\n"
        "You can check your Rental ID by clicking 'My rentals'."
    )

    await state.set_state(RentCarStates.waiting_for_return_rental_id)


@router.message(RentCarStates.waiting_for_return_rental_id)
async def return_car_get_rental_id(message: Message, state: FSMContext):
    try:
        rental_id = int(message.text)
    except ValueError:
        await message.answer("Please enter a valid Rental ID as a number.")
        return

    success, result_message = await return_rental(
        telegram_id=message.from_user.id,
        rental_id=rental_id
    )

    await message.answer(result_message)
    write_log(
    action="return_car",
    telegram_id=message.from_user.id,
    details=result_message
)
    await state.clear()


@router.message(F.text == "🛠 Report damage")
async def report_damage_handler(message: Message, state: FSMContext):
    await message.answer(
        "Please enter the Rental ID for the damage report.\n\n"
        "You can check your Rental ID by clicking 'My rentals'."
    )

    await state.set_state(RentCarStates.waiting_for_damage_rental_id)


@router.message(RentCarStates.waiting_for_damage_rental_id)
async def report_damage_get_rental_id(message: Message, state: FSMContext):
    try:
        rental_id = int(message.text)
    except ValueError:
        await message.answer("Please enter a valid Rental ID as a number.")
        return

    await state.update_data(rental_id=rental_id)

    await message.answer(
        "Please describe the damage.\n\n"
        "Example: Small scratch on the front bumper."
    )

    await state.set_state(RentCarStates.waiting_for_damage_description)


@router.message(RentCarStates.waiting_for_damage_description)
async def report_damage_get_description(message: Message, state: FSMContext):
    description = message.text.strip()

    if len(description) < 5:
        await message.answer("Description is too short. Please describe the damage in more detail.")
        return

    data = await state.get_data()
    rental_id = data["rental_id"]

    success, result_message = await create_damage_report(
        telegram_id=message.from_user.id,
        rental_id=rental_id,
        description=description
    )

    await message.answer(result_message)

    write_log(
        action="report_damage",
        telegram_id=message.from_user.id,
        details=result_message
    )

    await state.clear()


@router.message(F.photo)
async def photo_handler(message: Message, state: FSMContext):
    await message.answer("Nice photo! But this bot works with car rentals 😊")
    await state.clear()

