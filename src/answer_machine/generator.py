import telebot
import json


class AnswerGenerator:
    """AnswerGenerator class. It is used to provide a reply for user's input.
    Also AnswerGenerator interacts with db:
      - adds user information;
      - removes users;
      - checks whether user is registred or not;
      - gets user's schedule using API endpoint from db.
    """
    rdb = None
    """This is a db controller class instance"""
    answers_template = None
    """This is the path to .json file, which contains all bot's replies."""


    def __init__(self, rdb, answers_template):
        """AnswerGenerator's class constructor. Takes 2 arguments: rdb instance
        and .json replies file path."""
        self.rdb = rdb
        with open(answers_template) as f:
            self.answers_template = json.load(f)


    def cmd_start(self, message):
        """This method is executed by bot.py when user sends /start message.
        It creates a new user in db(or erases user's information if user 
        already exists) and asks user to choose his role."""
        self.rdb.reg_user(message.chat.id, message.chat.first_name)

        markup = telebot.types.ReplyKeyboardMarkup()
        itembtn1 = telebot.types.KeyboardButton(
            self.answers_template["keyboard_student"]
        )
        itembtn2 = telebot.types.KeyboardButton(
            self.answers_template["keyboard_teacher"]
        )
        markup.add(itembtn1, itembtn2)
        return self.answers_template["/start"], markup


    def cmd_help(self, message):
        """This method is executed by bot.py when user sends /help message.
        Just returns help message from answers_template."""
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        return self.answers_template["/help"], markup


    def cmd_rozklad(self, message):
        """This method is executed by bot.py when user sends /rozklad message.
        Checks if user is registred and then sends user's schedule."""
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        user = self.rdb.get_user(message.chat.id)
        message = ""
        if user[3] == "":
            markup = telebot.types.ReplyKeyboardMarkup()
            itembtn1 = telebot.types.KeyboardButton(
            self.answers_template["keyboard_student"])
            itembtn2 = telebot.types.KeyboardButton(
            self.answers_template["keyboard_teacher"])
            markup.add(itembtn1, itembtn2)
            return self.answers_template["reg_student_teacher_choose"], markup

        elif user[3] == 1:
            if user[4] == "":
                return self.answers_template["reg_group_choose_err"], markup

            else:
                g = self.rdb.get_group_by_id(user[4])
                return self.answers_template["sending_schedule_group"].format(g[1]), markup, g[2]

        elif user[3] == 0:
            if user[5] == "":
                return self.answers_template["reg_surname_choose_err"], markup

            else:
                g = self.rdb.get_tname_by_id(user[5])
                return self.answers_template["sending_schedule_teacher"].format(g[1]), markup, g[2]


    def message(self, message):
        """Handles any other user's message. Used for registration."""
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        user = self.rdb.get_user(message.chat.id)
        if user[3] == "":
            if message.text == self.answers_template["keyboard_student"]:
                self.rdb.set_isStudent(message.chat.id, "1")
                return self.answers_template["reg_group_choose"], markup

            elif message.text == self.answers_template["keyboard_teacher"]:
                self.rdb.set_isStudent(message.chat.id, "0")
                return self.answers_template["reg_surname_choose"], markup

            markup = telebot.types.ReplyKeyboardMarkup()
            itembtn1 = telebot.types.KeyboardButton(
            self.answers_template["keyboard_student"])
            itembtn2 = telebot.types.KeyboardButton(
            self.answers_template["keyboard_teacher"])
            markup.add(itembtn1, itembtn2)
            return self.answers_template["reg_student_teacher_choose"], markup

        elif user[3] == 1:
            if user[4] == "":
                group = self.rdb.get_group(message.text.upper())
                if group == None:
                    return self.answers_template["group_not_found_err"], markup

                else:
                    self.rdb.set_group(message.chat.id, group[0])
                    return self.answers_template["reg_done"], markup

        elif user[3] == 0:
            if user[5] == "":
                name = self.rdb.get_tname(message.text)
                if name == None:
                    return self.answers_template["teacher_not_found_err"], markup

                else:
                    self.rdb.set_name(message.chat.id, name[0])
                    return self.answers_template["reg_done"], markup

