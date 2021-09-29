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
                f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&APPID=2a1fa51ed2d0b30a5e976b62e76638e3')
            weather = r.json()
            temp = int(int(weather["main"]["temp"])-272.15)
            w = weather["weather"]
            w = w[0].get("description")
            printweather = f"На данный момент в городе {city} {w}! Градусник показывает: {temp}°с"
            bot.send_message(message.chat.id, printweather)
        except:
            bot.send_message(
                message.chat.id, "Я не нашел ваш город =( Попробуй еще! /weather")


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)

        time.sleep(15)
