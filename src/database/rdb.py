import sqlite3
import datetime
import time


class RDB:
    def __init__(self):
        self.conn = sqlite3.connect("database/users.db", check_same_thread=False)
        self.cursor = self.conn.cursor()

    def reg_user(self, uid, uname):
        cuser = self.get_user(uid)
        time.sleep(0.1)
        if cuser != None:
            print("UPDATE")
            sql = "UPDATE users SET 'isStudent'='', 'group'='', 'name'='' WHERE id={}".format(
                cuser[0]
            )
        else:
            print("INSERT")
            sql = "INSERT INTO users ('uid', 'uname', 'isStudent', 'group', 'name') VALUES ({}, '{}', '', '', '')".format(
                uid, uname
            )
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("UID not unique")

    def get_user(self, uid):
        sql = "SELECT * FROM users WHERE uid={}".format(uid)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def set_isStudent(self, uid, s):
        sql = "UPDATE users SET 'isStudent'='{}' WHERE uid={}".format(s, uid)
        self.cursor.execute(sql)
        self.conn.commit()

    def set_group(self, uid, g):
        sql = "UPDATE users SET 'group'='{}' WHERE uid={}".format(g, uid)
        self.cursor.execute(sql)
        self.conn.commit()

    def set_name(self, uid, n):
        sql = "UPDATE users SET 'name'='{}' WHERE uid={}".format(n, uid)
        self.cursor.execute(sql)
        self.conn.commit()

    def get_group(self, gname):
        sql = "SELECT * FROM groups WHERE groupName='{}'".format(gname)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_tname(self, tname):
        sql = "SELECT * FROM teachers WHERE name='{}'".format(tname)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_group_by_id(self, id):
        sql = "SELECT * FROM groups WHERE id={}".format(id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_tname_by_id(self, id):
        sql = "SELECT * FROM teachers WHERE id={}".format(id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()
