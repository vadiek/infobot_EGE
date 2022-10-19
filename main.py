from unittest.mock import call

import telebot
from keyboa.keyboards import keyboa_maker

from libs.telebot import types
from keyboa import Keyboa

bot = telebot.TeleBot('5504467462:AAFM21r5kFEX9PmVhg8j308cvDYykknm1hU')


@bot.message_handler(commands=['start'])
def start(message):

    buttons = [
        ('Информация о ЕГЭ', '01'), ('Расписание ЕГЭ', '02'), ('Минимальные баллы', '03'),
        ('Баллы для поступления', '04'), ('Баллы за прошлый год', '05'), ('Где можно посмотреть результаты', '06'),
        ('Перевод первичных баллов', '07')
    ]

    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1)

    bot.send_message(message.chat.id,
                     'Привет, пользователь, данный бот создан для информирования пользователей о различных аспектах ЕГЭ \n'
                     '\nНиже представлен список доступной информации, нажимая на кнопки вы будете получать информацию нужную вам',
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '01':
        print('1')
    elif call.data == '02':
        print('2')
    elif call.data == '03':
        print('3')
    elif call.data == '04':
        print('4')
    elif call.data == '05':
        print('5')
    elif call.data == '06':
        print('6')
    elif call.data == '07':
        print('7')
bot.polling(none_stop=True)
