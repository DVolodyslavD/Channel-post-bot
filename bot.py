import os

from aiogram import types
import aiogram.utils.markdown as fmt

from config import dp, bot, CHANNEL_ID, OWNER_ID


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    pass


@dp.message_handler(commands=['post_pblc_pls'])
async def post_publication_command(message: types.Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        return
    else:
        img = '' #image link
        post = f'''{fmt.hide_link(img)}</a>''' #youre text
        await bot.send_message(CHANNEL_ID, post)


@dp.message_handler()
async def for_other_messages(message: types.Message):
    if message.content_type == "text":
        post = message.text
        await bot.send_message(CHANNEL_ID, post)