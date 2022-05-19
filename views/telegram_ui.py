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
    data.insert_user(
        message.chat.id, 
        make_string(message.chat.first_name),
        make_string(message.chat.last_name),
        make_string(message.chat.username),
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
    if message.chat.type == 'private':
        value_type = 1
        user_id = message.chat.id
        data.insert_user(
            message.chat.id, 
            make_string(message.chat.first_name),
            make_string(message.chat.last_name),
            make_string(message.chat.username),
        )
    elif message.chat.type == 'supergroup':
        value_type = 2
        user_id = message.chat.id
        data.insert_group(
            message.chat.id, 
            make_string(message.chat.title)
        )
    if message.forward_from_chat and message.forward_from_chat.type == 'channel':
        value_type = 3
        user_id = message.forward_from_chat.id
        data.insert_channel(
            message.forward_from_chat.id,
            make_string(message.forward_from_chat.title), 
            make_string(message.forward_from_chat.username)
        )

    joke_id, joke_str = data.return_random_joke(user_id, value_type)
    await bot.send_message(user_id, joke_str)
    data.insert_user_joke(
        message.chat.id, 
        value_type, 
        joke_id
    )

@dp.message_handler()
async def callback_menu_main(message:Message):
    if message.chat.type == 'private':
        value_type = 1
        user_id = message.chat.id
        data.insert_user(
            message.chat.id, 
            make_string(message.chat.first_name),
            make_string(message.chat.last_name),
            make_string(message.chat.username),
        )
    elif message.chat.type == 'supergroup':
        value_type = 2
        user_id = message.chat.id
        data.insert_group(
            message.chat.id, 
            make_string(message.chat.title)
        )
    if message.forward_from_chat and message.forward_from_chat.type == 'channel':
        value_type = 3
        user_id = message.forward_from_chat.id
        data.insert_channel(
            message.forward_from_chat.id,
            make_string(message.forward_from_chat.title), 
            make_string(message.forward_from_chat.username)
        )
    
    if message.text.strip() == TelegramButtons.send or value_type == 3:
        joke_id, joke_str = data.return_random_joke(user_id, value_type)
        await bot.send_message(user_id, joke_str)
        data.insert_user_joke(
            user_id, 
            value_type, 
            joke_id
        )

    if message.text.strip() == TelegramButtons.history:
        await message.answer('Your hos')
        return
