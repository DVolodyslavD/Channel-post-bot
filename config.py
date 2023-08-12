
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

TOKEN = '' #bot token

OWNER_ID = 00000 #youre telegram id (admin/owner id)
CHANNEL_ID = 00000 #youre channel id

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
