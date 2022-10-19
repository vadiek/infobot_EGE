from unittest.mock import call

import telebot
from keyboa.keyboards import keyboa_maker

from libs.telebot import types
from keyboa import Keyboa

bot = telebot.TeleBot('5504467462:AAFM21r5kFEX9PmVhg8j308cvDYykknm1hU')


@bot.message_handler(commands=['start'])
def start(message):

    buttons = [
        'Информация о ЕГЭ', 'Расписание ЕГЭ', 'Минимальные баллы',
        'Баллы для поступления', 'Баллы за прошлый год', 'Где можно посмотреть результаты',
        'Перевод первичных баллов'
    ]

    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1)

    bot.send_message(message.chat.id,
                     'Привет, пользователь, данный бот создан для информирования пользователей о различных аспектах ЕГЭ \n'
                     '\nНиже представлен список доступной информации, нажимая на кнопки вы будете получать информацию нужную вам',
                     reply_markup=markup)

bot.polling(none_stop=True)
