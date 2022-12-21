# Код с кнопками

import telebot
from telebot import types
from config import TOKEN

lazertag_pars_bot = telebot.TeleBot(TOKEN)


def get_butt(*name):
    butt = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Хранение кнопок
    try:
        button1 = types.KeyboardButton(name[0])  # Кнопка 1
        button2 = types.KeyboardButton(name[1])  # Кнопка 2
        butt.add(button1, button2)  # Дабавление кнопок
    except IndexError:
        button1 = types.KeyboardButton(name[0])
        butt.add(button1)  # Дабавление добавление 1-й кнопки

    return butt


@lazertag_pars_bot.message_handler(commands=['start'])

def start(message):
    lazertag_pars_bot.send_message(message.chat.id, 'Добрый день, выберите режим', reply_markup=get_butt('Фильтр', 'Рассылка'))

@lazertag_pars_bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Фильтр':
        lazertag_pars_bot.send_message(message.chat.id, 'Выберите режим', reply_markup=get_butt('Пользователи (до 3-х суток)', 'Пользователи группы')) # Кнопка 1 - Пользователи, которые были недавно в сети (до 3-х суток). Кнопка 2 - Пользователи конкретной группы
    elif message.text == 'Пользователи (до 3-х суток)':
        lazertag_pars_bot.send_message(message.chat.id, 'Выберите режим', reply_markup=get_butt('Отправка данных')) # Кнопка - Выбор режима отправки данных пользователей

    elif message.text == 'Рассылка':
        lazertag_pars_bot.send_message(message.chat.id, 'Выберите режим', reply_markup=get_butt('Записать в файл', 'Добавить в ручную')) # Кнопка 1 - Ввод ссылок через файл, запись большого количесва ссылок. Кнопка 2 - Ввод ссылок через Бота, запись по одной ссылке введённой в ручную

    elif message.text == 'Записать в файл':
        # TODO: Записать в файл
        lazertag_pars_bot.send_message(message.chat.id, 'Выберите режим', reply_markup=get_butt('Фильтр', 'Рассылка'))




lazertag_pars_bot.polling(none_stop=True)



