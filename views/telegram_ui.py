from aiogram.types import (
    Message, 
    ParseMode, 
    CallbackQuery
)
from views.telegram_bot import (
    dp, 
    bot, 
    data
)
from views.telegram_utilities import menu_main
from utilities.work_files import make_string
from config import ( 
    TelegramButtons,
    TelegramCommands,
    TelegramMessages,
)


@dp.message_handler(commands=[TelegramCommands.start])
async def start_message(message:Message):
    """
    Function to start the converstation between values
    """
    id = message.chat.id
    name_first = make_string(message.chat.first_name)
    name_last = make_string(message.chat.last_name)
    username = make_string(message.chat.username)

    data.insert_user(
        id, 
        name_first, 
        name_last, 
        username
    )
    await message.answer(TelegramMessages.start, reply_markup=menu_main)

@dp.message_handler(commands=[TelegramCommands.history])
async def start_history(message:Message):
    """
    Function to add the selected user for the 
    """
    await message.answer("Номер:")

@dp.message_handler(commands=[TelegramCommands.send])
async def start_settings(message:Message):
    """
    Function to add the selected user for the 
    """
    await message.answer("Номер:")


@dp.message_handler()#CheckMessageFilter())
async def callback_menu_main(message:Message):
    
    if message.text.strip() == TelegramButtons.send:
        await message.answer("fdfghfghfghfgh")
        data.return_random_joke(message.chat.id, 1)
        return

    if message.text.strip() == TelegramButtons.history:
        await message.answer('Your hos')
        return
