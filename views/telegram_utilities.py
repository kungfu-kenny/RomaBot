from aiogram.types import (
    ReplyKeyboardMarkup, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup
)
from config import TelegramButtons


menu_main = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    keyboard=[
        [
            InlineKeyboardButton(TelegramButtons.send, callback_data='100'),
        ],
        [
            InlineKeyboardButton(TelegramButtons.history, callback_data='101'),
        ],
    ]
)