import telebot
import sqlite3
from telebot import types


def films_button(set_of_films, keyboard_markup):          # KEYBOARD MARKUP

    for film in set_of_films:
        keyboard_markup.add(types.KeyboardButton(str(film)[2:-3]))

    return keyboard_markup


conn = sqlite3.connect("movies.db")      # GETTING INFORMATION FROM DATABASE
cursor = conn.cursor()
sql = "SELECT movie FROM movies"
cursor.execute(sql)
films_set = set(cursor.fetchall())


bot = telebot.TeleBot('965005174:AAFV2x1XtLxzTACxKOOaun9ShEkDoiq88bw')

markup = types.ReplyKeyboardMarkup(row_width=2)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # bot.send_message(message.from_user.id, "Сегодня в кино:")

    # for film in films_set:
    #     bot.send_message(message.from_user.id, film)

    bot.send_message(message.from_user.id,
                     "Перед вами список фильмов на сегодня. Выберите фильм, "
                     "чье расписание вы хотели бы увидеть: ",
                     reply_markup=films_button(films_set, markup))


bot.polling(none_stop=True, interval=0)
