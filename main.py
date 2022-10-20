from unittest.mock import call

import telebot
from keyboa.keyboards import keyboa_maker
from libs.telebot import types
from keyboa import Keyboa


def info(id):
    buttons = [
        ('Продолжительность', '101'), ('Что можно брать с собой?', '102'), ('Список обязательных предметов', '103'),
        ('<== Назад', '104')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1)
    bot.send_message(id, 'Информация о ЕГЭ', reply_markup=markup)


def dates(id):
    bot.send_message(id, 'Даты егэ')


def min_bal(id):
    bot.send_message(id, 'Минимальные баллы')


def bal_g(id):
    buttons = [
        ('Средние баллы поступающих за прошлый год', '201'), ('Баллы в самые популярные ВУЗы', '202'), ('Минимальные баллы для поступления', '203'),
        ('<== Назад', '204')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1)
    bot.send_message(id, "Баллы для поступления", reply_markup=markup)


def last_bal(id):
    buttons = [
        ('Средние баллы во всей старне 2022', '301'), ('Средние баллы в регионе 2022', '302'), ('Количество стобальников', '303'),
        ('<== Назад', '304')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1)
    bot.send_message(id, 'Баллы за прошлый год', reply_markup=markup)


def result(id):

    bot.send_message(id, 'РЦОИ')


def refactor_bal(id):
    buttons = [
        ('Схема переводов', '401'), ('Критерии оценки', '402'),
        ('<== Назад', '404')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1)
    bot.send_message(id, 'Информация о ЕГЭ', reply_markup=markup)


bot = telebot.TeleBot('5504467462:AAFM21r5kFEX9PmVhg8j308cvDYykknm1hU')


@bot.message_handler(commands=['start'])
def start(message):
    buttons = [
        ('Информация о ЕГЭ', '01'), ('Расписание ЕГЭ', '02'), ('Минимальные баллы', '03'),
        ('Баллы для поступления', '04'), ('Баллы за прошлый год', '05'), ('Где можно посмотреть результаты', '06'),
        ('Перевод первичных баллов', '07')
    ]

    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1)
    print(message.chat.id)

    bot.send_message(message.chat.id,
                     'Привет, пользователь, данный бот создан для информирования пользователей о различных аспектах ЕГЭ \n'
                     '\nНиже представлен список доступной информации, нажимая на кнопки вы будете получать информацию нужную вам',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call)
    if call.data == '01':
        info(call.from_user.id)
    elif call.data == '02':
        dates(call.from_user.id)
    elif call.data == '03':
        min_bal(call.from_user.id)
    elif call.data == '04':
        bal_g(call.from_user.id)
    elif call.data == '05':
        last_bal(call.from_user.id)
    elif call.data == '06':
        result(call.from_user.id)
    elif call.data == '07':
        refactor_bal(call.from_user.id)


bot.polling(none_stop=True)
