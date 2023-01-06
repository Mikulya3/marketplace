from aiogram.dispatcher.filters import Command
from aiogram.types import Message, update

# from applications.telegrammbot.models import BotUser
from main import dp, bot
from config import admin_id

import requests


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.reply("Привет!")
    data = requests.get('http://localhost:8000/api/v1/product/').json()
    results = data['results']
    msg = ''
    for product in results:
        msg += f'{product["name"]} --> {product["price"]}\n'
    await bot.send_message(message.chat.id, msg)
    # BotUser.objects.get_or_create(message.chat.id)

# @dp.message_handler(Command('sendall'))
# async def send_all(message: Message):
#     if message.chat.id == admin_id:
#         await message.answer('Start')
#         # if message.chat.id not in BotUser:
#         #     await message.answer('Start')
#         #     user = message.from_user.id
#         #     users.append(user)
#         for user in BotUser.objects.all():
#             # await bot.send_message(user.chat, message.text[message.text.find(' '):])
#             await bot.send_message(user.chat, 'Helllooooooo')
#         # for user in users:
#         #     await bot.send_message(user, message.text[message.text.find(' '):])
#         await message.answer('Done')
#     else:
#         await message.answer('Error')
        # while True:
        #     response = requests.get("http://someurl.com", timeout=60)
        #     for message in response:
        #         bot.answer(message)