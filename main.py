from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from pprint import pprint
import requests
import telebot
import time
from telebot import types
bot = telebot.TeleBot('2048875525:AAFwUQ5otU0g_MSsGNoNJvUfnH7RilgWa3I')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id, "Привет,я бот который показывает погоду! Что бы узнать погоду /weather")


sity = None


@bot.message_handler(commands=['weather'])
def handle_text(message):
    bot.send_message(message.chat.id, "Погода в каком городе вас интересует?")

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        try:
            city = message.text
            r = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=2a1fa51ed2d0b30a5e976b62e76638e3')
            weather = r.json()
            temp = int(int(weather["main"]["temp"])-273.15)
            printweather = f"Погода в городе {city} в данный момент: {temp} градусов"
            bot.send_message(message.chat.id, printweather)
        except:
            bot.send_message(
                message.chat.id, "Я не нашел ваш город =( Попробуй еще! /weather")


button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)

        time.sleep(15)
