from aiogram import Bot, Dispatcher
from config import EnvVariables


bot = Bot(token=EnvVariables.token)
dp = Dispatcher(bot)