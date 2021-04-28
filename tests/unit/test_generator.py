import json

import sys
sys.path.append('./answer_machine')
sys.path.append('./database')

import rdb
import generator
import telebot

db = rdb.RDB()
ag = generator.AnswerGenerator(db, "answer_machine/templates/ru.json")

with open("answer_machine/templates/ru.json") as f:
    answers_template = json.load(f)

class Message:
    def __init__(self, chat, message):
        self.text = message
        self.chat = chat

class Chat:
    def __init__(self, id, first_name):
        self.id = id
        self.first_name = first_name

def test_cmd_start():
    message = Message(Chat(1, "Pytest"), "")
    reply = ag.cmd_start(message)
    assert reply[0] == answers_template["/start"]


def test_student():
    test_cmd_start()
    message = Message(Chat(1, "Pytest"), answers_template["keyboard_student"])
    reply = ag.message(message)
    assert reply[0] == answers_template["reg_group_choose"]

def test_teacher():
    test_cmd_start()
    message = Message(Chat(1, "Pytest"), answers_template["keyboard_teacher"])
    reply = ag.message(message)
    assert reply[0] == answers_template["reg_surname_choose"]


def test_wrong_group():
    test_student()
    message = Message(Chat(1, "Pytest"), "io-00")
    reply = ag.message(message)
    assert reply[0] == answers_template["group_not_found_err"]

def test_wrong_surname():
    test_teacher()
    message = Message(Chat(1, "Pytest"), "surname")
    reply = ag.message(message)
    assert reply[0] == answers_template["teacher_not_found_err"]


def test_right_group():
    test_student()
    message = Message(Chat(1, "Pytest"), "io-91")
    reply = ag.message(message)
    assert reply[0] == answers_template["reg_done"]


def test_rozklad():
    test_right_group()
    message = Message(Chat(1, "Pytest"), "")
    reply = ag.cmd_rozklad(message)
    assert reply[0] == answers_template["sending_schedule_group"].format("IO-91")


def test_help():
    message = Message(Chat(1, "Pytest"), "")
    reply = ag.cmd_help(message)
    assert reply[0] == answers_template["/help"]
