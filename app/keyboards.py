from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚗 Available cars"),
            KeyboardButton(text="📅 Rent car"),
        ],
        [
            KeyboardButton(text="📋 My rentals"),
            KeyboardButton(text="🔁 Return car"),
        ],
        [
            KeyboardButton(text="🛠 Report damage"),
            KeyboardButton(text="ℹ️ Help"),
        ],
        [
            KeyboardButton(text="🤖 AI Assistant"),
        ],
    ],
    resize_keyboard=True
)


ai_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Back to menu"),
        ],
    ],
    resize_keyboard=True
)