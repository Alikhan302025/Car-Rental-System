from aiogram import Router, types
from aiogram.filters import Command
from app.keyboards import main_menu

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Welcome!", reply_markup=main_menu)