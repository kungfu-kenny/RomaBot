from aiogram import executor
from parsers.parse_manually import ParseManually
from parsers.parse_citaty import ParseCitaty
from parsers.parse_anekdoty import ParseAnekdoty
from models.db_use import DataUsage
# from views.telegram_ui import dp
from config import EnvVariables


try:
    for cls in [
        ParseManually,
        ParseCitaty,
        ParseAnekdoty
    ]:
        cls().develop_parse_main(EnvVariables.noncheck)
    df_check = cls().develop_df_all()
    
    d = DataUsage(
        EnvVariables.postgesql,
        EnvVariables.create_db
    )
    d.insert_jokes_database(df_check)
    # executor.start_polling(dp, skip_updates=True)

except Exception as e:
    print(e)
    print('..............................................1')