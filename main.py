import telebot

bot = telebot.TeleBot('5504467462:AAFM21r5kFEX9PmVhg8j308cvDYykknm1hU')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, пользователь')