from aiogram.types import (
    Message, 
    ParseMode, 
    CallbackQuery
)
from views.telegram_bot import dp, bot
from config import ( 
    TelegramButtons,
    TelegramCommands,
)


@dp.message_handler(commands=[TelegramCommands.start])
async def start_message(message:Message):
    """
    Function to add the selected user for the 
    """
    await message.answer("Номер:")

@dp.message_handler(commands=[TelegramCommands.history])
async def start_history(message:Message):
    """
    Function to add the selected user for the 
    """
    await message.answer("Номер:")

@dp.message_handler(commands=[TelegramCommands.settings])
async def start_settings(message:Message):
    """
    Function to add the selected user for the 
    """
    await message.answer("Номер:")
