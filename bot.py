import telebot

bot = telebot.TeleBot('965005174:AAFV2x1XtLxzTACxKOOaun9ShEkDoiq88bw')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, Тося, я тебя люблю, спасибо что протестила")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
