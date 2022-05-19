import asyncio
import schedule
from time import sleep
from aiogram import executor
from parsers.parse_manually import ParseManually
from views.telegram_ui import (
    dp, 
    bot, 
    data
)
from config import EnvVariables


async def make_group_values_message(loop) -> set:
    """
    Function which is dedicated to get required values
    """
    value_ids = data.select_id_send()
    for res, t in value_ids:
        joke_id, joke_str = data.return_random_joke(res, t)
        await bot.send_message(res, joke_str)
        data.insert_user_joke(
            res, 
            t, 
            joke_id
        )

def main():
    ParseManually().develop_parse_main(EnvVariables.noncheck)
    df_check = ParseManually().develop_df_all()
    data.insert_jokes_database(df_check)
    loop = asyncio.get_event_loop()
    executor.start(dp, make_group_values_message(loop), skip_updates=True)


if __name__ == '__main__':
    schedule.every().day.at("12:30").do(main)
    while True:
        schedule.run_pending()
        sleep(1)
