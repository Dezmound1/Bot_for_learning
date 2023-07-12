from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
import json

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
#
class Dict_subjects:
    "Класс создания списков включенных и выключенных предметов"
    def __init__(self, database):
        self.database = database

    def get_subjects_by_status(self, status):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute("SELECT id, title FROM subject WHERE status = ?", (status,))
        subjects = {key : value for key, value in cursor.fetchall()}
        cursor.close()
        conn.close()
        return subjects
database_file = 'example.db'

subjects = Dict_subjects(database_file)
true_subjects = subjects.get_subjects_by_status(True)
false_subjects = subjects.get_subjects_by_status(False)

on = []
off = []
class Make_butt:
    def __init__(self):
        self.dict = dict

    def make_on(self, dict):
        for key, value in dict.items():
                on.append([InlineKeyboardButton(
                                text= value,
                                callback_data= key)
                        ])
    def make_off(self, dict):
        for key, value in dict.items():
            off.append([InlineKeyboardButton(
                                text= value,
                                callback_data= key)
                        ])

dict_on = Make_butt()
dict_on.make_on(true_subjects)

dict_off = Make_butt()
dict_off.make_off(false_subjects)


# cursor.execute('''CREATE TABLE IF NOT EXISTS subject
#                 (id INTEGER PRIMARY KEY, title TEXT, status INTEGER, cost INTEGER,
#                 schedule TEXT, room INTEGER, teacher TEXT, comment TEXT)''')
#
# with open('data.json', encoding='utf-8') as json_file:
#     data = json.load(json_file)
#
# for key, value in data.items():
#     sql = '''INSERT INTO subject (id, title, status, cost, schedule, room, teacher, comment)
#              VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
#     params = (int(key), value["title"], int(value["status"]), value["cost"],
#               value["schedule"], value["room"], value["teacher"], value["comment"])
#     cursor.execute(sql, params)
# conn.commit()
# cursor.close()
# conn.close()
