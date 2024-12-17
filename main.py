import requests
import json
# api_url = 'http://127.0.0.1:8000/api/convert/'
# api_url = 'https://79c3-84-54-83-43.ngrok-free.app/api/convert/'
#
# import logging
#
# from aiogram import Bot, Dispatcher, executor, types
#
# API_TOKEN = '7863489354:AAGUF-Gy_p2Os3jMsbnzdJkhg8WyFTKkrR0'
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Assalomu aleykum")


# @dp.message_handler()
# async def echo(message: types.Message):
#     # if isinstance(int(message.text), int):
#         data = {
#             'number': int(message.text)
#         }
#         response = requests.post(api_url, json=data)
#         print(response.text)
#         # await message.answer(response.json['number_in_words'])
#         r = json.loads(response.text)['number_in_words']
#         await message.answer(r)
#     # else:
#     #     print(message.text)
#     #     await message.answer('Enter only number...')
import requests
import json
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7863489354:AAGUF-Gy_p2Os3jMsbnzdJkhg8WyFTKkrR0'
api_url = 'https://2330-185-139-138-223.ngrok-free.app/api/convert/'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum")

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():  # Check if input is a number
        data = {
            'number': int(message.text)
        }
        response = requests.post(api_url, json=data)
        print(response.status_code)  # Log the status code
        print(response.json())          # Log the response text for debugging

        if response.status_code == 200:
            try:
                r = response.json()  # Use .json() directly
                await message.answer(r['number_in_words'])
            except json.JSONDecodeError:
                await message.answer("Error decoding the response!")
        else:
            await message.answer("Error: Received status code " + str(response.status_code))
    else:
        await message.answer('Enter only number...')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
