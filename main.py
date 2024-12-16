import requests
import json
# api_url = 'http://127.0.0.1:8000/api/convert/'
api_url = 'https://79c3-84-54-83-43.ngrok-free.app/api/convert/'

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7863489354:AAGUF-Gy_p2Os3jMsbnzdJkhg8WyFTKkrR0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum")


@dp.message_handler()
async def echo(message: types.Message):
    # if isinstance(int(message.text), int):
        data = {
            'number': int(message.text)
        }
        response = requests.post(api_url, json=data)
        print(response.text)
        # await message.answer(response.json['number_in_words'])
        r = json.loads(response.text)['number_in_words']
        await message.answer(r)
    # else:
    #     print(message.text)
    #     await message.answer('Enter only number...')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
