from telebot import TeleBot, types
import os

# Токен бота
bot = TeleBot('')


# /start
@bot.message_handler(commands=['start'])
def main(message):
    welcome_text = ()
    
    bot.send_message(message.chat.id, welcome_text)

bot.polling(none_stop=True)
