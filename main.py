import telebot
from telebot import types

bot = telebot.TeleBot('5504467462:AAFM21r5kFEX9PmVhg8j308cvDYykknm1hU')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    f_button = types.InlineKeyboardButton('Информация о ЕГЭ', callback_data='1')
    s_button = types.InlineKeyboardButton('Расписание ЕГЭ', callback_data='1')
    t_button = types.InlineKeyboardButton('Минимальные баллы', callback_data='1')
    forth_button = types.InlineKeyboardButton('Баллы для поступления', callback_data='1')
    fifth_button = types.InlineKeyboardButton('Баллы за прошлый год', callback_data='1')
    sixes_button = types.InlineKeyboardButton('Где можно посмотреть результаты', callback_data='1')
    seventh_button = types.InlineKeyboardButton('Перевод первичных баллов', callback_data='1')

    markup.add(f_button, s_button, t_button, forth_button, fifth_button, sixes_button, seventh_button)

    bot.send_message(message.chat.id,
                     'Привет, пользователь, данный бот создан для информирования пользователей о различных аспектах ЕГЭ \n'
                     '\nНиже представлен список доступной информации, нажимая на кнопки вы будете получать информацию нужную вам',
                     reply_markup=markup)


bot.polling(none_stop=True)