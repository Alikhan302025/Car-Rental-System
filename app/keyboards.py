from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Available cars"),
            KeyboardButton(text="Rent car"),
        ],
        [
            KeyboardButton(text="My rentals"),
            KeyboardButton(text="Return car"),
        ],
        [
            KeyboardButton(text="Report damage"),
            KeyboardButton(text="Help"),
        ],
    ],
    resize_keyboard=True
)