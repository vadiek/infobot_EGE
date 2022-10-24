from unittest.mock import call

import telebot
from keyboa.keyboards import keyboa_maker
from libs.telebot import types
from keyboa import Keyboa


def clean(ch_id, message_id, bot_t):
    bot_t.delete_message(chat_id=ch_id, message_id=message_id)
    print('ok')


def info(id, mes_id, ch_id):
    buttons = [
        ('Продолжительность', '101'), ('Что можно брать с собой?', '102'), ('Список обязательных предметов', '103'),
        ('<== Назад', '104')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1, front_marker=str(mes_id)+'/'+ str(ch_id) + '/')
    bot.send_message(id, 'Информация о ЕГЭ', reply_markup=markup)


def dates(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '704')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1, front_marker=str(mes_id)+'/'+ str(ch_id) + '/')
    bot.send_message(id, 'Даты егэ', reply_markup=markup)


def min_bal(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '604')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1, front_marker=str(mes_id)+'/'+ str(ch_id) + '/')
    bot.send_message(id, 'Минимальные баллы', reply_markup=markup)


def bal_g(id, mes_id, ch_id):
    buttons = [
        ('Средние баллы поступающих за прошлый год', '201'), ('Баллы в самые популярные ВУЗы', '202'),
        ('Минимальные баллы для поступления', '203'),
        ('<== Назад', '204')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1, front_marker=str(mes_id)+'/'+ str(ch_id) + '/')
    bot.send_message(id, "Баллы для поступления", reply_markup=markup)


def last_bal(id, mes_id, ch_id):
    buttons = [
        ('Средние баллы во всей старне 2022', '301'), ('Средние баллы в регионе 2022', '302'),
        ('Количество стобальников', '303'),
        ('<== Назад', '304')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1, front_marker=str(mes_id)+'/'+ str(ch_id) + '/')
    bot.send_message(id, 'Баллы за прошлый год', reply_markup=markup)


def result(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '504')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1, front_marker=str(mes_id)+'/'+ str(ch_id) + '/')
    bot.send_message(id, 'РЦОИ', reply_markup=markup)

def refactor_bal(id, mes_id, ch_id):
    buttons = [
        ('Схема переводов', '401'), ('Критерии оценки', '402'),
        ('<== Назад', '404')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1, front_marker=str(mes_id)+'/'+ str(ch_id) + '/')
    bot.send_message(id, 'Информация о ЕГЭ', reply_markup=markup)

def start1(id, mes_id, ch_id):
    buttons = [
        ('Информация о ЕГЭ', '01'), ('Расписание ЕГЭ', '02'), ('Минимальные баллы', '03'),
        ('Баллы для поступления', '04'), ('Баллы за прошлый год', '05'), ('Где можно посмотреть результаты', '06'),
        ('Перевод первичных баллов', '07')
    ]

    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1, front_marker=str(mes_id)+'/'+ str(ch_id) + '/')

    bot.send_message(id,
                     'Привет, пользователь, данный бот создан для информирования пользователей о различных аспектах ЕГЭ \n'
                     '\nНиже представлен список доступной информации, нажимая на кнопки вы будете получать информацию нужную вам',
                     reply_markup=markup)


bot = telebot.TeleBot('5504467462:AAFM21r5kFEX9PmVhg8j308cvDYykknm1hU')


@bot.message_handler(commands=['start'])
def start(message):
    buttons = [
        ('Информация о ЕГЭ', '01'), ('Расписание ЕГЭ', '02'), ('Минимальные баллы', '03'),
        ('Баллы для поступления', '04'), ('Баллы за прошлый год', '05'), ('Где можно посмотреть результаты', '06'),
        ('Перевод первичных баллов', '07')
    ]

    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1, front_marker=str(message.id)+'/'+ str(message.chat.id) + '/')
    print(message.id)

    bot.send_message(message.chat.id,
                     'Привет, пользователь, данный бот создан для информирования пользователей о различных аспектах ЕГЭ \n'
                     '\nНиже представлен список доступной информации, нажимая на кнопки вы будете получать информацию нужную вам',
                     reply_markup=markup)
    print(type(message.chat.id), type(message.id))

    clean(message.chat.id, message.id, bot)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    str = call.data
    list = str.split('/')
    mes_id = int(list[0]) + 1
    ch_id = int(list[1])
    if list[2] == '01':
        info(call.from_user.id, mes_id, ch_id)
    elif list[2] == '02':
        dates(call.from_user.id, mes_id, ch_id)
    elif list[2] == '03':
        min_bal(call.from_user.id, mes_id, ch_id)
    elif list[2] == '04':
        bal_g(call.from_user.id, mes_id, ch_id)
    elif list[2] == '05':
        last_bal(call.from_user.id, mes_id, ch_id)
    elif list[2] == '06':
        result(call.from_user.id, mes_id, ch_id)
    elif list[2] == '07':
        refactor_bal(call.from_user.id, mes_id, ch_id)
    elif list[2] == '104' or list[2] == '204' or list[2] == '304' or list[2] == '404' or list[2] == '504' or list[2] == '604' or list[2] == '704':
        start1(call.from_user.id, mes_id, ch_id)
    clean(ch_id, mes_id, bot)


bot.polling(none_stop=True)
