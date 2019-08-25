import telebot
from telebot.apihelper import ApiException
import sqlite3
from telebot import types
import re


def films_button(set_of_films, keyboard_markup):          # КЛАВИША ДЛЯ КЛАВИАТУРЫ

    for film in set_of_films:
        keyboard_markup.add(types.KeyboardButton(str(film).strip("()'',")))

    return keyboard_markup


def get_timetable(message):
    a = []
    with sqlite3.connect("movies.db") as con:
        cur = con.cursor()
        for row in cur.execute("SELECT time, cinema FROM movies WHERE movie=(?)", (message, )):
            a.append(row)

    b = re.sub(",", "\n", str(a))
    c = re.sub("[()''[\]]", " ", b)
    return c


conn = sqlite3.connect("movies.db", check_same_thread=False)      # ПОЛУЧЕНИЕ ИНФОРМАЦИИ С БАЗЫ ДАННЫХ
cursor = conn.cursor()
sql = "SELECT movie FROM movies"
cursor.execute(sql)
films_set = set(cursor.fetchall())

bot = telebot.TeleBot('965005174:AAFV2x1XtLxzTACxKOOaun9ShEkDoiq88bw')


remove_markup = types.ReplyKeyboardRemove(selective=False)


@bot.message_handler(commands=['start', 'help'])
def get_text_messages(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=False, resize_keyboard=True)
    bot.send_message(message.from_user.id,
                     "Перед вами список фильмов на сегодня. Выберите фильм, "
                     "расписание которого вы хотели бы увидеть: ",
                     reply_markup=films_button(films_set, markup))


@bot.message_handler(func=lambda message: True)
def send_timetable(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=False, resize_keyboard=True)
    except_markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=False, resize_keyboard=True)
    if len(get_timetable(message.text)) > 4096:
        for x in range(0, len(get_timetable(message.text)), 4096):
            bot.send_message(message.from_user.id, get_timetable(message.text)[x:x + 4096],
                             reply_markup=films_button(films_set, markup))
    else:

        try:
            bot.send_message(message.from_user.id, get_timetable(message.text),
                             reply_markup=films_button(films_set, markup))

        except ApiException:
            bot.send_message(message.from_user.id, "Вы выбрали фильм на который нет сеансов,"
                                                   " попробуйте другой!", reply_markup=films_button(films_set, except_markup))


bot.polling(none_stop=True, interval=0)
