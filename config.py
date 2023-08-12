
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

TOKEN = ''

OWNER_ID = 00000
CHANNEL_ID = 00000

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
