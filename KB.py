<<<<<<< HEAD
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

Menu = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Авторизоваться",callback_data='stud')]
        ]
)
Option = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Авторизоваться",callback_data='verification')]
        ]
)
Сourse = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Редактировать курсы",callback_data= 'open')],
                [InlineKeyboardButton(text="Открыть/Зактрыть курсы",callback_data= 'closed')]
        ]
)
on_off = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Открытые курсы",callback_data= 'open_butt')],
                [InlineKeyboardButton(text="Закрытые курсы",callback_data= 'closed')]
        ]
)
Menu_return = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Авторизоваться как студент",callback_data= 'stud')]
        ]
)
yes_no = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="✅Включить✅",callback_data= 'ans_yes')],
                [InlineKeyboardButton(text="❌Выключить❌",callback_data= 'ans_no')]
        ]
)
#Кнопки для линии студентов
stud_button = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, keyboard=[
                [KeyboardButton(text= "FAQ")],
                [KeyboardButton(text= "Открытые курсы")],
                [KeyboardButton(text= "Мои курсы")],
                [KeyboardButton(text= "Личные данные")]

        ]
)
faq_button = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="О Боте",callback_data= 'about')],
                [InlineKeyboardButton(text="Политика обработки ПДн",callback_data= 'politic')]
        ]
)
back_button = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Назад",callback_data= 'back_faq')]
        ]
)
about_user_buttons = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, keyboard=[
                [KeyboardButton(text= "ФИО")],
                [KeyboardButton(text= "Группа")],
                [KeyboardButton(text= "Номер телефона")],
                [KeyboardButton(text= "Дата рождения")],
                [KeyboardButton(text= "Серия паспорта")],
                [KeyboardButton(text= "Номер паспорта")],
                [KeyboardButton(text= "Дата выдачи")],
                [KeyboardButton(text= "Кем выдан")],
                [KeyboardButton(text= "Код подразделения")],
                [KeyboardButton(text= "Место регистрации")],
                [KeyboardButton(text= "Назад")]

        ]
)
cours_info = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="👨🏻‍🎓‍ЗАПИСАТЬСЯ👩🏼‍🎓",callback_data= 'load')],
                [InlineKeyboardButton(text="стоимость",callback_data= 'cost')],
                [InlineKeyboardButton(text="рассписание",callback_data= 'schedule')],
                [InlineKeyboardButton(text="аудитория",callback_data= 'room')],
                [InlineKeyboardButton(text="преподаватель",callback_data= 'teacher')],
                [InlineKeyboardButton(text="комментарий",callback_data= 'comment')],
                [InlineKeyboardButton(text="Назад",callback_data= 'back_list')]
        ]
)
return_info = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Назад",callback_data= 'return_info')]
        ]
)
answer = InlineKeyboardMarkup(row_width=2, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="да",callback_data= 'yes')],
                [InlineKeyboardButton(text="нет",callback_data= 'no')]
        ]
=======
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

Menu = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Авторизоваться",callback_data='stud')]
        ]
)
Option = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Авторизоваться",callback_data='verification')],
                [InlineKeyboardButton(text="Назад",callback_data='back')]
        ]
)
Сourse = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Редактировать курсы",callback_data= 'open')],
                [InlineKeyboardButton(text="Открыть/Зактрыть курсы",callback_data= 'closed')]
        ]
)
on_off = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Открытые курсы",callback_data= 'open_butt')],
                [InlineKeyboardButton(text="Закрытые курсы",callback_data= 'closed')]
        ]
)
Menu_return = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Авторизоваться как студент",callback_data= 'stud')]
        ]
)
yes_no = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="✅Включить✅",callback_data= 'ans_yes')],
                [InlineKeyboardButton(text="❌Выключить❌",callback_data= 'ans_no')]
        ]
)
#Кнопки для линии студентов
stud_button = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, keyboard=[
                [KeyboardButton(text= "FAQ")],
                [KeyboardButton(text= "Открытые курсы")],
                [KeyboardButton(text= "Мои курсы")],
                [KeyboardButton(text= "Личные данные")]

        ]
)
faq_button = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="О Боте",callback_data= 'about')],
                [InlineKeyboardButton(text="Политика обработки ПДн",callback_data= 'politic')]
        ]
)
back_button = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Назад",callback_data= 'back_faq')]
        ]
)
about_user_buttons = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, keyboard=[
                [KeyboardButton(text= "ФИО")],
                [KeyboardButton(text= "Группа")],
                [KeyboardButton(text= "Номер телефона")],
                [KeyboardButton(text= "Дата рождения")],
                [KeyboardButton(text= "Номер паспорта")],
                [KeyboardButton(text= "Серия паспорта")],
                [KeyboardButton(text= "Дата выдачи")],
                [KeyboardButton(text= "Кем выдан")],
                [KeyboardButton(text= "Код подразделения")],
                [KeyboardButton(text= "Место регистрации")],
                [KeyboardButton(text= "Назад")]

        ]
)
cours_info = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="👨🏻‍🎓‍ЗАПИСАТЬСЯ👩🏼‍🎓",callback_data= 'load')],
                [InlineKeyboardButton(text="стоимость",callback_data= 'cost')],
                [InlineKeyboardButton(text="рассписание",callback_data= 'schedule')],
                [InlineKeyboardButton(text="аудитория",callback_data= 'room')],
                [InlineKeyboardButton(text="преподаватель",callback_data= 'teacher')],
                [InlineKeyboardButton(text="комментарий",callback_data= 'comment')],
                [InlineKeyboardButton(text="Назад",callback_data= 'back_list')]
        ]
)
return_info = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="Назад",callback_data= 'return_info')]
        ]
)
answer = InlineKeyboardMarkup(row_width=2, resize_keyboard=True,
        inline_keyboard=[
                [InlineKeyboardButton(text="да",callback_data= 'yes')],
                [InlineKeyboardButton(text="нет",callback_data= 'no')]
        ]
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
)