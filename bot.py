import telebot
import sqlite3
from telebot import types
from pprint import pprint
import re


def films_button(set_of_films, keyboard_markup):          # KEYBOARD MARKUP

    for film in set_of_films:
        keyboard_markup.add(types.KeyboardButton(str(film).strip("()'',")))

    return keyboard_markup


def get_timetable(message):
    a = []
    with sqlite3.connect("movies.db") as con:
        cur = con.cursor()
        for row in cur.execute("SELECT time, cinema FROM movies WHERE movie=(?)", (message, )):
            a.append(row)

    pprint(a)
    b = re.sub("[()''[\]]", " ", str(a))
    return b


conn = sqlite3.connect("movies.db", check_same_thread = False)      # GETTING INFORMATION FROM DATABASE
cursor = conn.cursor()
sql = "SELECT movie FROM movies"
cursor.execute(sql)
films_set = set(cursor.fetchall())


bot = telebot.TeleBot('965005174:AAFV2x1XtLxzTACxKOOaun9ShEkDoiq88bw')

markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)


@bot.message_handler(commands=['start', 'help'])
def get_text_messages(message):
    # bot.send_message(message.from_user.id, "Сегодня в кино:")

    # for film in films_set:
    #     bot.send_message(message.from_user.id, film)

    bot.send_message(message.from_user.id,
                     "Перед вами список фильмов на сегодня. Выберите фильм, "
                     "чье расписание вы хотели бы увидеть: ",
                     reply_markup=films_button(films_set, markup),)


@bot.message_handler(func=lambda message: True)
def send_timetable(message):
    # for time, cinema in get_timetable(message.text):
    #     bot.send_message(message.from_user.id, (time, cinema))

    bot.send_message(message.from_user.id, get_timetable(message.text))


bot.polling(none_stop=True, interval=0)
