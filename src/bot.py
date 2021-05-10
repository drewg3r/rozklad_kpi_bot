"""
## Programm structure
bot.py handles all the messages users send to bot. Then it uses `AnswerGenerator`
to get the reply to user's command. This file contains message handlers. 

## Executing the bot
To execute, you need to provide bot's `SECRET_TOKEN` using environment variable.
In Linux:
```
export ROZKLAD_BOT_KEY=xxx
```
Then just run bot.py:
```
python3 ./bot.py
```
---
"""

import telebot
import os
import database.rdb as rdb
import answer_machine.generator as answer_generator


db = rdb.RDB()
"""Selecting file containing all bot's answers."""

ag = answer_generator.AnswerGenerator(db, "answer_machine/templates/ru.json")
"""Setting up the `AnswerGenerator`. Specifying file with bot's answers."""

bot = telebot.TeleBot(os.environ.get('ROZKLAD_BOT_KEY'))
"""Getting bot `SECRET_TOKEN` from system environment variable."""


@bot.message_handler(commands=["start"])
def reg_new_user(message):
    """[note]: 123
    Handles the **/start** comand.
    Clears user info from db, if there is any.
    Asks user to choose: he is a student or a teacher."""
    reply = ag.cmd_start(message)
    bot.send_message(message.chat.id, reply[0], reply_markup=reply[1]) # Send message back to user


@bot.message_handler(commands=["help"])
def help_cmd(message):
    """Handles the **/help** comand.
    Just sends the help message, specified in `answer_machine/templates/lang.json`"""
    reply = ag.cmd_help(message)
    bot.send_message(message.chat.id, reply[0], reply_markup=reply[1]) # Send message back to user


@bot.message_handler(commands=["rozklad"])
def rozklad_cmd(message):
    """Handles the **/rozklad** comand.
    Sends user's schedule, if user is already registred. Otherwise sends
    registration prompt."""
    reply = ag.cmd_rozklad(message)
    bot.send_message(message.chat.id, reply[0], reply_markup=reply[1]) # Send message back to user
    bot.send_photo(message.chat.id, open(reply[2], 'rb')) # Send picture with schedule


@bot.message_handler(func=lambda message: message.text[0] != "/", content_types=["text"])
def handle_text(message):
    """Handles **any other** message, which is not a command."""
    reply = ag.message(message)
    bot.send_message(message.chat.id, reply[0], reply_markup=reply[1]) # Send message back to user


# bot.infinity_polling(True)
