from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import FromJsonToDB

Menu = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                    text= "Администратор",
                    callback_data= 'admin'
                        )
                ],
                [
                InlineKeyboardButton(
                    text= "Студент",
                    callback_data= 'stud'
                        )
                ]
        ]
)
Menu_return = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                    text= "Авторизоваться как студент",
                    callback_data= 'stud'
                        )
                ]
        ]
)

Option = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                    text= "Авторизоваться",
                    callback_data= 'verification'
                        )
                ],
                [
                InlineKeyboardButton(
                    text= "Назад",
                    callback_data= 'back'
                        )
                ]
        ]
)

Сourse = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                    text= "Редактировать курсы",
                    callback_data= 'open'
                        )
                ],
                [
                InlineKeyboardButton(
                    text= "Открыть/Зактрыть курсы",
                    callback_data= 'closed'
                        )
                ]
        ]
)

on_off = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                    text= "Открытые курсы",
                    callback_data= 'open'
                        )
                ],
                [
                InlineKeyboardButton(
                    text= "Закрытые курсы",
                    callback_data= 'closed'
                        )
                ]
        ]
)

ask_me_off = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                    text= "Да",
                    callback_data= 'yes'
                        )
                ],
                [
                InlineKeyboardButton(
                    text= "Вернуться",
                    callback_data= 'back'
                        )
                ]
        ]
)

ask_me_on = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                    text= "Да",
                    callback_data= 'yes'
                        )
                ],
                [
                InlineKeyboardButton(
                    text= "Вернуться",
                    callback_data= 'back'
                        )
                ]
        ]
)

Open_course = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard= FromJsonToDB.on)
Closed_course = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard= FromJsonToDB.off)