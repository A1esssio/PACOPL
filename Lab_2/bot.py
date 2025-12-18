"""
Telegram bot example with button keyboard.
Implements a simple Telegram bot using pyTelegramBotAPI.
"""

import telebot
from telebot import types

# Insert your token here
API_TOKEN = "TOKEN"
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message: telebot.types.Message):
    """
    Handles /start command and sends a reply keyboard with options.
    """

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_greet = types.KeyboardButton("Hello")
    btn_help = types.KeyboardButton("Help")
    keyboard.add(btn_greet, btn_help)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def echo_all(message: telebot.types.Message):
    """
    Handles all user messages and responds by button selected.
    """
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Hello! How can I help you?")
    elif message.text == "Help":
        bot.send_message(
            message.chat.id,
            "This is a simple bot with buttons. Use the buttons to interact.",
        )


bot.polling()
