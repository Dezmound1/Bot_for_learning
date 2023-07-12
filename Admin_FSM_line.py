import time
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import *
from Module import dp, KB, list_of_colums
import re
import sqlite3
import SQLiteClass
import FromJsonToDB


class Admin_FSM(StatesGroup):
#_______________________Вход в админа_______________________
	catching_text = State()
	cheking_data = State()
#________Состояния для изменения информации по курсам_______
	course = State()
	change_option = State()
	type_set = State()
	cost_it = State()
	schedule_it = State()
	room_it = State()
	teacher_it = State()
	comment_it = State()
#______________Состояния для статусов по курсам_____________
	set_status = State()
	catch_click_off = State()
	catch_click_on = State()
	apdate_off = State()
	apdate_on = State()

con = sqlite3.connect("example.db")
cur = con.cursor()




async def cmd_cancel(message: types.Message, state= FSMContext):
    await state.finish()


async def came_data(callback: types.CallbackQuery, state= Admin_FSM.catching_text):
	async with state.proxy() as data:
		data["button"] = callback.data
		data["data_id"] = callback.from_user.id
	await callback.message.answer("Введите пароль!")
	await Admin_FSM.cheking_data.set()

async def coming_text(message: types.Message, state = Admin_FSM.cheking_data):
	async with state.proxy() as data:
		data["message"] = message.text
	cur.execute(f"""SELECT password FROM admin WHERE id = {data["data_id"]}""")
	result = cur.fetchall()
	if data["message"] == result[0][0]:
		await message.answer("Вы правильно ввели пароль, проходите дальше!", reply_markup= KB.Сourse)
		await Admin_FSM.course.set()
	else:
		await message.answer("НЕВЕРНЫЙ ПАРОЛЬ!!\nВведите повторно или пройдите регистрацию, как студент!", reply_markup= KB.Menu_return)

async def cours_type(callback: types.CallbackQuery, state= Admin_FSM.course):
	async with state.proxy() as data:
		data["button"] = callback.data
	if data["button"] == "open":
		await callback.message.edit_text("Список открытых курсов!", reply_markup= KB.Open_course)
		await Admin_FSM.change_option.set()
	else:
		await callback.message.answer("Выбери тип курсов!", reply_markup= KB.on_off) #Вызов изменений закрытия\открытия курсов
		await Admin_FSM.set_status.set()

#____________Пропись ВКЛ\ВЫКЛ имеющихся курсов____________
async def press_but(callback: types.CallbackQuery, state= Admin_FSM.set_status):
	async with state.proxy() as data:
		data["button_status"] = callback.data
	if data["button_status"] == "open":
		await callback.message.edit_text("Список открытых курсов!", reply_markup= KB.Open_course)
		await Admin_FSM.catch_click_off.set()
	else:
		await callback.message.edit_text("Список закрытых курсов!", reply_markup= KB.Closed_course)
		await Admin_FSM.catch_click_on.set()


async def click_butt_off(callback: types.CallbackQuery, state= Admin_FSM.catch_click_off):
	async with state.proxy() as data:
		data["subject"] = callback.data
	await callback.message.edit_text("Ты точно хотите отключить запись?", reply_markup= KB.ask_me_off)
	await Admin_FSM.apdate_off.set()

async def answer_off(callback: types.CallbackQuery, state= Admin_FSM.apdate_off):
	async with state.proxy() as data:
		data["answer"] = callback.data
	update_data = f"""UPDATE subject SET status = False WHERE id = {data["subject"]} """
	cur.execute(update_data)
	con.commit()
	true_subjects = FromJsonToDB.subjects.get_subjects_by_status(True)
	FromJsonToDB.dict_on.make_on(true_subjects)
	await callback.message.edit_text("Список открытых курсов!", reply_markup= KB.Open_course)
	await Admin_FSM.set_status.set()

async def click_butt_on(callback: types.CallbackQuery, state= Admin_FSM.catch_click_on):
	async with state.proxy() as data:
		data["subject"] = callback.data
	await callback.message.edit_text("Ты точно хотите отключить запись?", reply_markup= KB.ask_me_on)
	await Admin_FSM.apdate_on.set()

async def answer_on(callback: types.CallbackQuery, state= Admin_FSM.apdate_on):
	async with state.proxy() as data:
		data["answer"] = callback.data
	update_data = f"""UPDATE subject SET status = True WHERE id = {data["subject"]} """
	cur.execute(update_data)
	con.commit()
	false_subjects = FromJsonToDB.subjects.get_subjects_by_status(False)
	FromJsonToDB.dict_on.make_on(false_subjects)
	await callback.message.edit_text("Список закрытых курсов!", reply_markup= KB.Closed_course)
	await Admin_FSM.set_status.set()

#_________________НАПИСАНИЕ РЕДАКТИРОВАНИЯ ИНФОРМАЦИИ О ПРЕДМЕТАХ___________________
async def options(callback: types.CallbackQuery, state= Admin_FSM.change_option):
	async with state.proxy() as data:
		data['callback'] = callback.data
	await callback.message.edit_text("Выбирите данные для изменения!", reply_markup= list_of_colums.changing)
	await Admin_FSM.type_set.set()

#Изменение Стоимости
async def cost_set(callback: types.CallbackQuery, state= Admin_FSM.type_set):
	async with state.proxy() as data:
		data["data_option"] = callback.data
	cur.execute(f"""SELECT {data["data_option"]} FROM subject WHERE id = {data['callback']}""")
	result = cur.fetchone()
	await callback.message.answer(f"Введи новую стоимость!\nСтоимость курса сейчас {result[0]} рублей!")
	await Admin_FSM.cost_it.set()
	SQLiteClass.db.write_log("Я здесь побывал!")

async def cost_it(message: types.Message, state=Admin_FSM.cost_it):
	async with state.proxy() as data:
		data["text"] = message.text
	SQLiteClass.db.write_log(f"Стоимость курса = {message.text}")
	if re.fullmatch(r'\d{4,}', message.text): #цена не может быть меньше 4-х значного числа КАК ПРАВИЛО!
		update_data = f"""UPDATE subject SET {data['data_option']} = {message.text} WHERE id = {data['callback']} """
		cur.execute(update_data)
		con.commit()
		await message.answer("Ты изменил кост!")
		await message.answer("Выбери данные для изменения!", reply_markup= list_of_colums.changing)
		await Admin_FSM.type_set.set()
	else:
		await message.answer("Введи правильную стоимость!")

#Изменение даты
async def schedule_set(callback: types.CallbackQuery, state= Admin_FSM.type_set):
	async with state.proxy() as data:
		data["data_option"] = callback.data
	cur.execute(f"""SELECT {data["data_option"]} FROM subject WHERE id = {data['callback']}""")
	result = cur.fetchone()
	await callback.message.answer(f"Введи новую дату!\nДата курса сейчас {result[0]}!")
	await Admin_FSM.schedule_it.set()

async def schedule_it(message: types.Message, state=Admin_FSM.schedule_it):
	async with state.proxy() as data:
		data["text"] = message.text
	SQLiteClass.db.write_log(f"{time.asctime()} Дата курса = {message.text}")
	if re.fullmatch(r'(([0-2][1-9])|3+[0-1])+[.]+((0+[1-9])|[10-12])+[.]+(202+[3-8])', message.text):
		update_data = f"""UPDATE subject SET {data['data_option']} = '{message.text}' WHERE id = {data['callback']} """
		cur.execute(update_data)
		con.commit()
		await message.answer("Ты изменил дату!")
		await message.answer("Выбери данные для изменения!", reply_markup= list_of_colums.changing)
		await Admin_FSM.type_set.set()
	else:
		await message.answer("Введи правильную дату!")

#Изменение аудитории
async def room_set(callback: types.CallbackQuery, state= Admin_FSM.type_set):
	async with state.proxy() as data:
		data["data_option"] = callback.data
	cur.execute(f"""SELECT {data["data_option"]} FROM subject WHERE id = {data['callback']}""")
	result = cur.fetchone()
	await callback.message.answer(f"Введи новую аудиторию!\nАудитория курса сейчас {result[0]}!")
	await Admin_FSM.room_it.set()

async def room_it(message: types.Message, state=Admin_FSM.room_it):
	async with state.proxy() as data:
		data["text"] = message.text
	SQLiteClass.db.write_log(f"{time.asctime()} номер аудитории = {message.text}")
	if re.fullmatch(r'\d{4}', message.text):
		update_data = f"""UPDATE subject SET {data['data_option']} = '{message.text}' WHERE id = {data['callback']} """
		cur.execute(update_data)
		con.commit()
		await message.answer("Ты изменил номер аудитории!")
		await message.answer("Выбери данные для изменения!", reply_markup= list_of_colums.changing)
		await Admin_FSM.type_set.set()
	else:
		await message.answer("Введи правильный номер аудитории!")

#Изменение преподавателя
async def teacher_set(callback: types.CallbackQuery, state= Admin_FSM.type_set):
	async with state.proxy() as data:
		data["data_option"] = callback.data
	cur.execute(f"""SELECT {data["data_option"]} FROM subject WHERE id = {data['callback']}""")
	result = cur.fetchone()
	await callback.message.answer(f"Введи ФИО преподавателя!\nПреподаватель курса сейчас {result[0]}!")
	await Admin_FSM.teacher_it.set()

async def teacher_it(message: types.Message, state=Admin_FSM.teacher_it):
	async with state.proxy() as data:
		data["text"] = message.text
	SQLiteClass.db.write_log(f"{time.asctime()} ФИО преподавателя = {message.text}")
	if re.fullmatch(r'(\w{2,})+[ ]+(\w{2,})+[ ]+(\w{2,})', message.text):
		update_data = f"""UPDATE subject SET {data['data_option']} = '{message.text}' WHERE id = {data['callback']} """
		cur.execute(update_data)
		con.commit()
		await message.answer("Ты изменил ФИО преподавателя!")
		await message.answer("Выбери данные для изменения!", reply_markup= list_of_colums.changing)
		await Admin_FSM.type_set.set()
	else:
		await message.answer("Введи правильное ФИО преподавателя!")


#Изменение комментария
async def comment_set(callback: types.CallbackQuery, state= Admin_FSM.type_set):
	async with state.proxy() as data:
		data["data_option"] = callback.data
	cur.execute(f"""SELECT {data["data_option"]} FROM subject WHERE id = {data['callback']}""")
	result = cur.fetchone()
	await callback.message.answer(f"Введи комметарий!\nКомментарий для курса сейчас {result[0]}!")
	await Admin_FSM.comment_it.set()

async def comment_it(message: types.Message, state=Admin_FSM.comment_it):
	async with state.proxy() as data:
		data["text"] = message.text
	SQLiteClass.db.write_log(f"{time.asctime()} комментарий = {message.text}")
	update_data = f"""UPDATE subject SET {data['data_option']} = '{message.text}' WHERE id = {data['callback']} """
	cur.execute(update_data)
	con.commit()
	await message.answer("Ты изменил комментарий!")
	await message.answer("Выбери данные для изменения!", reply_markup= list_of_colums.changing)
	await Admin_FSM.type_set.set()

def admin_hendlers():
	dp.register_message_handler(cmd_cancel, commands='cancel', state= '*')
	dp.register_callback_query_handler(options, state=Admin_FSM.change_option)
	dp.register_callback_query_handler(came_data, text='verification', state=Admin_FSM.catching_text)
	dp.register_message_handler(coming_text, state=Admin_FSM.cheking_data)
	dp.register_callback_query_handler(cours_type, state=Admin_FSM.course)
	dp.register_callback_query_handler(cost_set,text = 'cost', state=Admin_FSM.type_set)
	dp.register_callback_query_handler(schedule_set,text = 'schedule', state=Admin_FSM.type_set)
	dp.register_callback_query_handler(room_set,text = 'room', state=Admin_FSM.type_set)
	dp.register_callback_query_handler(teacher_set,text = 'teacher', state=Admin_FSM.type_set)
	dp.register_callback_query_handler(comment_set,text = 'comment', state=Admin_FSM.type_set)
	dp.register_message_handler(cost_it, state=Admin_FSM.cost_it)
	dp.register_message_handler(schedule_it, state=Admin_FSM.schedule_it)
	dp.register_message_handler(room_it, state=Admin_FSM.room_it)
	dp.register_message_handler(teacher_it, state=Admin_FSM.teacher_it)
	dp.register_message_handler(comment_it, state=Admin_FSM.comment_it)
#Хэндлеры для Статусов по курсам
	dp.register_callback_query_handler(press_but, state=Admin_FSM.set_status)
	dp.register_callback_query_handler(click_butt_off, state = Admin_FSM.catch_click_off)
	dp.register_callback_query_handler(click_butt_on, state = Admin_FSM.catch_click_on)
	dp.register_callback_query_handler(answer_off, text = "yes", state = Admin_FSM.apdate_off)
	dp.register_callback_query_handler(answer_on, text = "yes", state = Admin_FSM.apdate_on)