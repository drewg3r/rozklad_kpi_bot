import telebot
import rdb
import time
import datetime

bot = telebot.TeleBot("1754531840:AAG-xgT6zIWgBKlMioyqNTsV3GF2GRExe0E")
db = rdb.RDB()

print(
    "{} Started!".format(
        time.strftime("[%H:%M:%S]", time.localtime()),
    )
)


@bot.message_handler(commands=["start"])
def reg_new_user(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    itembtn1 = telebot.types.KeyboardButton("Студент")
    itembtn2 = telebot.types.KeyboardButton("Преподаватель")
    markup.add(itembtn1, itembtn2)
    bot.send_message(
        message.chat.id,
        "Добро пожаловать! Давайте знакомиться. Вы...",
        reply_markup=markup,
    )
    print(
        "{} {}({}): {}".format(
            time.strftime("[%H:%M:%S]", time.localtime()),
            message.chat.first_name,
            message.chat.id,
            message.text,
        )
    )
    db.reg_user(message.chat.id, message.chat.first_name)


@bot.message_handler(
    func=lambda message: message.text[0] != "/",
    content_types=["text"],
)
def handle_text(message):
    markup = telebot.types.ReplyKeyboardRemove(selective=False)
    user = db.get_user(message.chat.id)
    if user[3] == "":
        if message.text == "Студент":
            db.set_isStudent(message.chat.id, "1")
            bot.send_message(
                message.chat.id,
                "Отлично! Теперь укажите свою группу в формате XX-00",
                reply_markup=markup,
            )
            return
        elif message.text == "Преподаватель":
            db.set_isStudent(message.chat.id, "0")
            bot.send_message(
                message.chat.id,
                "Отлично! Теперь укажите вашу фамилию и инициалы(например: Болдак А. О.)",
                reply_markup=markup,
            )
            return
        markup = telebot.types.ReplyKeyboardMarkup()
        itembtn1 = telebot.types.KeyboardButton("Студент")
        itembtn2 = telebot.types.KeyboardButton("Преподаватель")
        markup.add(itembtn1, itembtn2)
        bot.send_message(
            message.chat.id,
            "Выберите: вы студент или преподаватель...",
            reply_markup=markup,
        )

    elif user[3] == 1:
        if user[4] == "":
            group = db.get_group(message.text)
            if group == None:
                bot.send_message(
                    message.chat.id,
                    "Группы с таким названием не найдено. Укажите свою группу в формате XX-00",
                    reply_markup=markup,
                )
            else:
                db.set_group(message.chat.id, group[0])
                bot.send_message(
                    message.chat.id,
                    "Вы успешно зарегистрировались",
                    reply_markup=markup,
                )
            return

    elif user[3] == 0:
        if user[5] == "":
            name = db.get_tname(message.text)
            if name == None:
                bot.send_message(
                    message.chat.id,
                    "Преподавателя с таким именем не найдено",
                    reply_markup=markup,
                )
            else:
                db.set_name(message.chat.id, name[0])
                bot.send_message(
                    message.chat.id,
                    "Вы успешно зарегистрировались",
                    reply_markup=markup,
                )
            return


@bot.message_handler(commands=["rozklad"])
def rozklad_cmd(message):
    user = db.get_user(message.chat.id)
    if user[3] == "":
        bot.send_message(
            message.chat.id,
            "Нам нужно узнать вас немного лучше. Напишите 1 если вы студент, 2 если преподаватель",
        )
        return
    elif user[3] == 1:
        if user[4] == "":
            bot.send_message(
                message.chat.id,
                "Нам нужно узнать вас немного лучше. Укажите свою группу в формате ХХ-00",
            )
            return
        else:
            g = db.get_group_by_id(user[4])
            bot.send_message(
                message.chat.id,
                "Высылаю расписание для студента группы {}".format(g[1]),
            )

    elif user[3] == 0:
        if user[5] == "":
            bot.send_message(
                message.chat.id,
                "Нам нужно узнать вас немного лучше. Укажите свою фамилию и инициалы",
            )
            return
        else:
            g = db.get_tname_by_id(user[5])
            bot.send_message(
                message.chat.id,
                "Высылаю расписание для преподавателя {}".format(g[1]),
            )


@bot.message_handler(commands=["help"])
def help_cmd(message):
    bot.send_message(
        message.chat.id,
        "Это справка по команде /help.\nСписок команд:\n/start - сбросить настройки\n/rozklad - получить расписание",
    )


bot.infinity_polling(True)
