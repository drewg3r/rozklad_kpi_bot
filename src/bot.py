import telebot
import os
import database.rdb as rdb
import time
import datetime
import answer_machine.generator as answer_generator

db = rdb.RDB()
ag = answer_generator.AnswerGenerator(db, "answer_machine/templates/ru.json")

bot = telebot.TeleBot(os.environ.get('ROZKLAD_BOT_KEY'))

print(
    "{} Started!".format(
        time.strftime("[%H:%M:%S]", time.localtime()),
    )
)


@bot.message_handler(commands=["start"])
def reg_new_user(message):
    reply = ag.cmd_start(message)
    bot.send_message(message.chat.id, reply[0], reply_markup=reply[1])


@bot.message_handler(commands=["help"])
def help_cmd(message):
    reply = ag.cmd_help(message)
    bot.send_message(message.chat.id, reply[0], reply_markup=reply[1])


@bot.message_handler(commands=["rozklad"])
def rozklad_cmd(message):
    reply = ag.cmd_rozklad(message)
    bot.send_message(message.chat.id, reply[0], reply_markup=reply[1])
    bot.send_photo(message.chat.id, open(reply[2], 'rb'))


@bot.message_handler(func=lambda message: message.text[0] != "/", content_types=["text"])
def handle_text(message):
    reply = ag.message(message)
    bot.send_message(message.chat.id, reply[0], reply_markup=reply[1])


bot.infinity_polling(True)
