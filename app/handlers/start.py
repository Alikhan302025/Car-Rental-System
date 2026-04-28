from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards import main_menu
from app.services.customer_service import get_or_create_customer

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await get_or_create_customer(message.from_user)

    await message.answer(
        "Welcome to KazAvto Rental Bot!\n\n"
        "Please choose an option from the menu below:",
        reply_markup=main_menu
    )