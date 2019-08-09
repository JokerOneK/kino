import telebot
import sqlite3
from telebot import types


# def films_button(set):
#     for film in set:
#         return types.KeyboardButton(str(film))


conn = sqlite3.connect("movies.db")
cursor = conn.cursor()
sql = "SELECT movie FROM movies"
cursor.execute(sql)
films_set = set(cursor.fetchall())


markup = types.ReplyKeyboardMarkup(row_width=2)


bot = telebot.TeleBot('965005174:AAFV2x1XtLxzTACxKOOaun9ShEkDoiq88bw')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Сегодня в кино:")
    for film in films_set:
        bot.send_message(message.from_user.id, film)
    # bot.send_message(message.from_user.id, "Choose the film: ", reply_markup=markup)


bot.polling(none_stop=True, interval=0)
