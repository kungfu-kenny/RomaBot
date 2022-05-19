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

def return_callback_history(value_id:int, value_calc:set, index:int=0) -> object:
    """
    Function which is dedicated to develop the callback values of the history
    Input:  value_id = id of the selected usage
            value_calc = calculated values
    Output: we created the inline keyboard
    """
    length, value_list, add_next, id_type = value_calc
    index = index % add_next
    index_prev = index - 1
    index_next = index + 1
    keyboard = [
        [
            InlineKeyboardButton(
                id,
                callback_data='-1'
            ),
            InlineKeyboardButton(
                'Resend',
                callback_data=f"100_{value_id}_{id}"
            )
        ]
        for id in value_list
    ]
    if add_next > 1:
        keyboard.append(
            [
                InlineKeyboardButton(
                    '⬅️',
                    callback_data=f'101_{value_id}_{id_type}_{index_prev}'
                ),
                InlineKeyboardButton(
                    f"{index + 1} / {add_next}",
                    callback_data= '-1'
                ),
                InlineKeyboardButton(
                    '➡️',
                    callback_data=f'101_{value_id}_{id_type}_{index_next}'
                )
            ]
        )
    return (
        f'Total Length: {length}\nChoose youre previous joke:\n', 
        InlineKeyboardMarkup(inline_keyboard=keyboard)
    )
