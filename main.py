from unittest.mock import call

import telebot
from keyboa.keyboards import keyboa_maker
from libs.telebot import types
from keyboa import Keyboa


def clean(ch_id, message_id, bot_t):
    bot_t.delete_message(chat_id=ch_id, message_id=message_id)
    print('ok')


# -----------------------------------------------------------------------------------------------------------------------

def info(id, mes_id, ch_id):
    buttons = [
        ('Продолжительность', '101'), ('Что можно брать с собой?', '102'), ('Список обязательных предметов', '103'),
        ('<== Назад', '104')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Информация о ЕГЭ', reply_markup=markup)


def latest(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '114')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, '<b>Продолжителньость экзаменов</b>\n\n'
                    '→ ЕГЭ по <b>русскому языку</b>: 3 часа 30 минут (210 минут)\n\n'
                    '→ ЕГЭ по <b>базовой математике</b>: 3 часа (180 минут)\n\n'
                    '→ ЕГЭ по <b>профильной математике</b>: 3 часа 55 минут (235 минут)\n\n'
                    '→ ЕГЭ по <b>обществознанию</b>: 3 часа (180 минут)\n\n'
                    '→ ЕГЭ по <b>физике</b>: 3 часа 55 минут (235 минут)\n\n'
                    '→ ЕГЭ по <b>информатике и ИКТ</b>: 3 часа 55 минут (235 минут)\n\n'
                    '→ ЕГЭ по <b>истории</b>: 3 часа (180 минут)\n\n'
                    '→ ЕГЭ по <b>химии</b>: 3 часа 30 минут (210 минут)\n\n'
                    '→ ЕГЭ по <b>биологии</b>: 3 часа 55 минут (235 минут)\n\n'
                    '→ ЕГЭ по <b>литературе</b>: 3 часа 55 минут (235 минут)\n\n'
                    '→ ЕГЭ по <b>географии</b>: 3 часа (180 минут)\n\n'
                    '→ «Письменная часть» ЕГЭ по иностранным языкам, за исключением китайского: 3 часа 10 минут (190 минут)\n\n'
                    '→ «Говорение» в ЕГЭ по иностранным языкам, за исключением китайского: 17 минут\n\n'
                    '→ «Письменная часть» ЕГЭ по китайскому языку: 3 часа (180 минут)\n\n'
                    '→ «Говорение» по китайскому языку: 14 минут'
                     , reply_markup=markup, parse_mode='html')


def items(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '114')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, '<b>Что можно брать с собой на ЕГЭ?</b> \n'
                         '→ паспорт;\n'
                         '→ чёрную гелевую ручку;\n'
                         '→ воду, шоколад, медицинские препараты и питание при необходимости;\n'
                         '→ медицинскую маску и перчатки (при желании);\n'
                         '→ линейку (на ЕГЭ по математике, физике и географии);\n'
                         '→ непрограммируемый калькулятор (на ЕГЭ по физике, химии и географии);\n'
                         '→ транспортир (на ЕГЭ по географии).\n'
                     , reply_markup=markup, parse_mode='html')


def important(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '114')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, '<b>Обязательные к сдачи предметы</b>\n'
                     'Обязательными к сдаче являются русский язык и математика (профиль/база),\n'
                         ' при сдаче профильной математики баллы идут к поступлению,\n'
                         ' а базовой получается оценка идущая в аттеста\n'
                     , reply_markup=markup, parse_mode='html')


# -----------------------------------------------------------------------------------------------------------------------

def dates(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '704')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, '<b>Даты егэ</b>\n'
                         '→ 26 мая (четверг) – география, литература, химия;\n'
                         '→ 30 мая (понедельник) – русский язык;\n'
                         '→ 31 мая (вторник) – русский язык;\n'
                         '→ 2 июня (четверг) – ЕГЭ по математике профильного уровня;\n'
                         '→ 3 июня (пятница) – ЕГЭ по математике базового уровня;\n'
                         '→ 6 июня (понедельник) – история, физика;\n'
                         '→ 9 июня (четверг) – обществознание;\n'
                         '→ 14 июня (вторник) – иностранные языки (за исключением раздела «Говорение»), биология;\n'
                         '→ 16 июня (четверг) – иностранные языки (раздел «Говорение»);\n'
                         '→ 17 июня (пятница) – иностранные языки (раздел «Говорение»);\n'
                         '→ 20 июня (понедельник) – информатика;\n'
                         '→ 21 июня (вторник) – информатика;\n'
                     , reply_markup=markup, parse_mode='html')


# -----------------------------------------------------------------------------------------------------------------------

def min_bal(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '604')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Минимальные баллы', reply_markup=markup)


# -----------------------------------------------------------------------------------------------------------------------

def bal_g(id, mes_id, ch_id):
    buttons = [
        ('Средние баллы поступающих за прошлый год', '201'), ('Баллы в самые популярные ВУЗы', '202'),
        ('Минимальные баллы для поступления', '203'),
        ('<== Назад', '204')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, "Баллы для поступления", reply_markup=markup)


def mid_b(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '214')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Даты егэ', reply_markup=markup)


def pop_b(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '214')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Даты егэ', reply_markup=markup)


def min_b_g(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '214')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Даты егэ', reply_markup=markup)


# -----------------------------------------------------------------------------------------------------------------------
def last_bal(id, mes_id, ch_id):
    buttons = [
        ('Средние баллы во всей старне 2022', '301'), ('Средние баллы в регионе 2022', '302'),
        ('Количество стобальников', '303'),
        ('<== Назад', '304')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Баллы за прошлый год', reply_markup=markup)


def s_country(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '314')
    ]


    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, '<b>Средние баллы ЕГЭ 2022</b>\n'
    '\n → Математика профильная: 56,9\n'
    '→ Русский язык: 68,3\n'
    '→ Физика: 54,1\n'
    '→ Обществознание: 59,9\n'
    '→ Литература: 60,8\n'
    '→ Химия: 54,3\n'
    '→ Информатика: 59,5\n'
    '→ География: 54,6\n'
    '→ Биология: 50,2\n'
    '→ История: 58\n'
    '→ Английский: 73,3', reply_markup=markup, parse_mode='html')


def s_region(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '314')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Даты егэ', reply_markup=markup)


def count_100(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '314')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Даты егэ', reply_markup=markup)


# -----------------------------------------------------------------------------------------------------------------------
def result(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '504')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'РЦОИ', reply_markup=markup)

# -----------------------------------------------------------------------------------------------------------------------
def refactor_bal(id, mes_id, ch_id):
    buttons = [
        ('Схема переводов', '401'), ('Критерии оценки', '402'),
        ('<== Назад', '404')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Информация о ЕГЭ', reply_markup=markup)

def re_b(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '414')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Даты егэ', reply_markup=markup)

def manual_b(id, mes_id, ch_id):
    buttons = [
        ('<== Назад', '414')
    ]
    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')
    bot.send_message(id, 'Даты егэ', reply_markup=markup)

# -----------------------------------------------------------------------------------------------------------------------
def start1(id, mes_id, ch_id):
    buttons = [
        ('Информация о ЕГЭ', '01'), ('Расписание ЕГЭ', '02'), ('Минимальные баллы', '03'),
        ('Баллы для поступления', '04'), ('Баллы за прошлый год', '05'), ('Где можно посмотреть результаты', '06'),
        ('Перевод первичных баллов', '07')
    ]

    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(mes_id) + '/' + str(ch_id) + '/')

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

    markup = keyboa_maker(items=buttons, copy_text_to_callback=True, items_in_row=1,
                          front_marker=str(message.id) + '/' + str(message.chat.id) + '/')
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
    if list[2] == '01' or list[2] == '114':
        info(call.from_user.id, mes_id, ch_id)
    elif list[2] == '02':
        dates(call.from_user.id, mes_id, ch_id)
    elif list[2] == '03':
        min_bal(call.from_user.id, mes_id, ch_id)
    elif list[2] == '04' or list[2] == '214':
        bal_g(call.from_user.id, mes_id, ch_id)
    elif list[2] == '05' or list[2] == '314':
        last_bal(call.from_user.id, mes_id, ch_id)
    elif list[2] == '06':
        result(call.from_user.id, mes_id, ch_id)
    elif list[2] == '07' or list[2] == '414':
        refactor_bal(call.from_user.id, mes_id, ch_id)
    # -----------------------------------------------------------------------------------------------------------------------
    elif list[2] == '101':
        latest(call.from_user.id, mes_id, ch_id)
    elif list[2] == '102':
        items(call.from_user.id, mes_id, ch_id)
    elif list[2] == '103':
        important(call.from_user.id, mes_id, ch_id)
    # -----------------------------------------------------------------------------------------------------------------------
    elif list[2] == '201':
        mid_b(call.from_user.id, mes_id, ch_id)
    elif list[2] == '202':
        pop_b(call.from_user.id, mes_id, ch_id)
    elif list[2] == '203':
        min_b_g(call.from_user.id, mes_id, ch_id)
    # -----------------------------------------------------------------------------------------------------------------------
    elif list[2] == '301':
        s_country(call.from_user.id, mes_id, ch_id)
    elif list[2] == '302':
        s_region(call.from_user.id, mes_id, ch_id)
    elif list[2] == '303':
        count_100(call.from_user.id, mes_id, ch_id)
    # -----------------------------------------------------------------------------------------------------------------------
    elif list[2] == '401':
        re_b(call.from_user.id, mes_id, ch_id)
    elif list[2] == '402':
        manual_b(call.from_user.id, mes_id, ch_id)

    elif list[2] == '104' or list[2] == '204' or list[2] == '304' or list[2] == '404' or list[2] == '504' or list[
        2] == '604' or list[2] == '704':
        start1(call.from_user.id, mes_id, ch_id)
    clean(ch_id, mes_id, bot)


bot.polling(none_stop=True)
