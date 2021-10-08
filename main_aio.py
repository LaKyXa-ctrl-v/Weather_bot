import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
# Объект бота
bot = Bot(token='2048875525:AAFwUQ5otU0g_MSsGNoNJvUfnH7RilgWa3I')
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Выбрать город")
    keyboard.add(button_1)
    await message.reply('Привет,я бот который показывает погоду! Что бы узнать погоду нажмите кнопку "Выбрать город"!', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text and 'Выбрать город' in message.text)
async def send(message):
    await message.reply("В каком городе вас интересует погода? Напиши название города!")

    @dp.message_handler()
    async def handler_city(message: types.Message):
        city = message.text

        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&APPID=2a1fa51ed2d0b30a5e976b62e76638e3')
        weather = r.json()
        temp = int(int(weather["main"]["temp"])-272.15)
        w = weather["weather"]
        w = w[0].get("description")
        printweather = f"На данный момент в городе {city} {w}! Градусник показывает: {temp}°с"
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_2 = types.KeyboardButton(text="Узнать погоду")
        keyboard.add(button_2)
        await message.reply(printweather)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
