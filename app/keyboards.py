from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Available cars")],
        [KeyboardButton(text = "My rentals")]
    ],
    resize_keyboard = True

)