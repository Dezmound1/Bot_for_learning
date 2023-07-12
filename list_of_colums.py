from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
table_name = 'subject'
cursor.execute(f"PRAGMA table_info({table_name})")
columns = cursor.fetchall()

column_names = [column[1] for column in columns[2:]]
conn.close()

column_dict = {
    'status': 'статус',
    'cost': 'стоимость',
    'schedule': 'дата',
    'room': 'аудитория',
    'teacher': 'преподаватель',
    'comment': 'комментарий'
}
translated_dict = {column_name: column_dict[column_name] for column_name in column_names}
button = []
for element in translated_dict:
    button.append([InlineKeyboardButton(text = translated_dict[element], callback_data= element)])
changing = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard= button)