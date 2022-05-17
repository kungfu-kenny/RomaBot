from aiogram import Bot, Dispatcher
from models.db_use import DataUsage
from config import EnvVariables


bot = Bot(token=EnvVariables.token)
dp = Dispatcher(bot)
data = DataUsage(
    EnvVariables.postgesql,
    EnvVariables.create_db
)