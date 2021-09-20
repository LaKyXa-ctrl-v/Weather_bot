
from flask import Flask, request
import telebot

bot = telebot.TeleBot('2048875525:AAFwUQ5otU0g_MSsGNoNJvUfnH7RilgWa3I')
bot.set_webhook(url="https://2749-176-110-46-211.ngrok.io")
app = Flask(__name__)


@app.route('/', methods=["POST"])
def webhook():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )
    return "ok"


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(commands=['play'])
def start_command(message):
    bot.send_message(message.chat.id, 'play opa opa')


@bot.message_handler(commands=[''])
def start_command(message):
    bot.send_message(message.chat.id, 'hmmm')


if __name__ == "__main__":
    app.run()
