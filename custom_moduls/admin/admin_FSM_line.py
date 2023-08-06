import time
from aiogram.dispatcher.filters.state import StatesGroup, State
from custom_moduls.database.sqliteclass import Database
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import *
from Module import dp, KB
import custom_moduls.admin.list_of_colums
import re
<<<<<<< HEAD
from custom_moduls.user.User_line import User_FSM
=======

>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
a = Database("Dolg_bot_bd")


class Admin_FSM(StatesGroup):
	catching_text = State()
	cheking_data = State()
	course = State()
	change_option = State()
	type_set = State()
	cost_it = State()
	schedule_it = State()
	room_it = State()
	teacher_it = State()
	comment_it = State()
	set_subjects = State()  # Включить\выключить кнопки
	set_status_on = State()
	set_status_off = State()
	set_answer_on = State()
	set_answer_off = State()


async def cmd_cancel(message: types.Message, state=FSMContext):
	await state.finish()
async def back(message: types.Message, state= FSMContext):
	await Admin_FSM.set_subjects.set()
	await message.answer("Выбери тип курсов!", reply_markup=KB.on_off)
	await message.answer("Вернись назад! 👉🏻/menu👈🏻")
async def menu(message: types.Message, state= FSMContext):
	await Admin_FSM.course.set()
	await message.answer("Ты вернулся в главное меню", reply_markup=KB.Сourse)

async def came_data(callback: types.CallbackQuery, state=Admin_FSM.catching_text):
	async with state.proxy() as data:
		data["button"] = callback.data
		data["data_id"] = callback.from_user.id
	await callback.message.answer("Введите пароль!")
	await Admin_FSM.cheking_data.set()

async def coming_text(message: types.Message, state=Admin_FSM.cheking_data):
	async with state.proxy() as data:
		data["message"] = message.text
	if data["message"] == a.get_pass(message.from_user.id)[0]:
		await message.answer("Вы правильно ввели пароль, проходите дальше!", reply_markup=KB.Сourse)
		await Admin_FSM.course.set()
	else:
		await message.answer("НЕВЕРНЫЙ ПАРОЛЬ!!\nВведите повторно или пройдите регистрацию, как студент!", reply_markup=KB.Menu_return)


async def cours_type(callback: types.CallbackQuery, state=Admin_FSM.course):
	async with state.proxy() as data:
		data["button"] = callback.data
	if data["button"] == "open":
		await callback.message.edit_text("Список открытых курсов!", reply_markup=a.gen_off_on_subject_but()["on"])
		await Admin_FSM.change_option.set()
		await callback.message.answer("Вернись назад! 👉🏻/menu👈🏻")
	else:
		await callback.message.answer("Выбери тип курсов!", reply_markup=KB.on_off)  # Вызов изменений закрытия\открытия курсов
		await Admin_FSM.set_subjects.set()
		await callback.message.answer("Или вернись назад! 👉🏻/menu👈🏻")


# _________________НАПИСАНИЕ РЕДАКТИРОВАНИЯ ИНФОРМАЦИИ О ПРЕДМЕТАХ___________________
async def options(callback: types.CallbackQuery, state=Admin_FSM.change_option):
	async with state.proxy() as data:
		data['callback'] = callback.data
<<<<<<< HEAD
	await callback.message.edit_text(text="Выбирите данные для изменения!", reply_markup=custom_moduls.admin.list_of_colums.changing)
=======
	await callback.message.edit_text(text="Выбирите данные для изменения!",
	                                 reply_markup=custom_moduls.admin.list_of_colums.changing)
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await Admin_FSM.type_set.set()


# Изменение Стоимости
async def cost_set(callback: types.CallbackQuery, state=Admin_FSM.type_set):
	async with state.proxy() as data:
<<<<<<< HEAD
		data['data_option'] = callback.data
	result = a.select_info_subject(data['data_option'], "subject", data['callback'])
	await callback.message.answer(text=f"Введи новую стоимость!\nСтоимость курса сейчас {result} рублей!")
=======
		data["data_option"] = callback.data
		print(data["data_option"])
	result = a.select_info_subject(data["data_option"], "subject", data['callback'])
	await callback.message.answer(text=f"Введи новую стоимость!\nСтоимость курса сейчас {result[0]} рублей!")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await Admin_FSM.cost_it.set()


async def cost_it(message: types.Message, state=Admin_FSM.cost_it):
	async with state.proxy() as data:
		data["text"] = message.text
	if re.fullmatch(r'\d{4,}', message.text):  # цена не может быть меньше 4-х значного числа КАК ПРАВИЛО!
		a.update_info(data['data_option'], message.text, data['callback'])
<<<<<<< HEAD
		result = a.select_info_subject(data['data_option'], "subject", data['callback'])
		await message.answer(f"Ты изменил кост!, Теперь его стоимость {result} рублей!")
		await message.answer(text="Выбери данные для изменения!", reply_markup=custom_moduls.admin.list_of_colums.changing)
=======
		result = a.select_info_subject(data["data_option"], "subject", data['callback'])
		await message.answer(f"Ты изменил кост!, Теперь его стоимость {result[0]} рублей!")
		await message.answer(text="Выбери данные для изменения!",
		                     reply_markup=custom_moduls.admin.list_of_colums.changing)
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
		await Admin_FSM.type_set.set()
	else:
		await message.answer("Введи правильную стоимость!")


# Изменение даты
async def schedule_set(callback: types.CallbackQuery, state=Admin_FSM.type_set):
	async with state.proxy() as data:
<<<<<<< HEAD
		data['data_option'] = callback.data
	result = a.select_info_subject(data['data_option'], "subject", data['callback'])
	await callback.message.answer(f"Введи новую дату!\nДата курса сейчас {result}!")
=======
		data["data_option"] = callback.data
	result = a.select_info_subject(data["data_option"], "subject", data['callback'])
	await callback.message.answer(f"Введи новую дату!\nДата курса сейчас {result[0]}!")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await Admin_FSM.schedule_it.set()


async def schedule_it(message: types.Message, state=Admin_FSM.schedule_it):
	async with state.proxy() as data:
<<<<<<< HEAD
		data['text'] = message.text
	if re.fullmatch(r'(([0-2][1-9])|3+[0-1])+[.]+((0+[1-9])|[10-12])+[.]+(202+[3-8])', message.text):
		def formated_date(date):
			day, month, year = date.split(".")
			formatted_date = f"{year}.{month.zfill(2)}.{day.zfill(2)}"
			return formatted_date
		a.update_info(data['data_option'], formated_date(message.text), data['callback'])
		result = a.select_info_subject(data['data_option'], "subject", data['callback'])
		await message.answer(f"Ты изменил дату! Курс будет проводиться {result} числа!")
=======
		data["text"] = message.text
	if re.fullmatch(r'(([0-2][1-9])|3+[0-1])+[.]+((0+[1-9])|[10-12])+[.]+(202+[3-8])', message.text):
		a.update_info(data['data_option'], str(message.text), data['callback'])
		result = a.select_info_subject(data["data_option"], "subject", data['callback'])
		await message.answer(f"Ты изменил дату! Курс будет проводиться {result[0]} числа!")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
		await message.answer("Выбери данные для изменения!", reply_markup=custom_moduls.admin.list_of_colums.changing)
		await Admin_FSM.type_set.set()
	else:
		await message.answer("Введи правильную дату!")


# Изменение аудитории
async def room_set(callback: types.CallbackQuery, state=Admin_FSM.type_set):
	async with state.proxy() as data:
<<<<<<< HEAD
		data['data_option'] = callback.data
	result = a.select_info_subject(data['data_option'], "subject", data['callback'])
	await callback.message.answer(f"Введи новую аудиторию!\nАудитория курса сейчас {result}!")
=======
		data["data_option"] = callback.data
	result = a.select_info_subject(data["data_option"], "subject", data['callback'])
	await callback.message.answer(f"Введи новую аудиторию!\nАудитория курса сейчас {result[0]}!")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await Admin_FSM.room_it.set()


async def room_it(message: types.Message, state=Admin_FSM.room_it):
	async with state.proxy() as data:
<<<<<<< HEAD
		data['text'] = message.text
	if re.fullmatch(r'\d{4}', message.text):
		a.update_info(data['data_option'], message.text, data['callback'])
		result = a.select_info_subject(data['data_option'], "subject", data['callback'])
		await message.answer(f"Ты изменил номер аудитории! Курс будет проходить в аудитории № {result}!")
=======
		data["text"] = message.text
	if re.fullmatch(r'\d{4}', message.text):
		a.update_info(data['data_option'], message.text, data['callback'])
		result = a.select_info_subject(data["data_option"], "subject", data['callback'])
		await message.answer(f"Ты изменил номер аудитории! Курс будет проходить в аудитории № {result[0]}!")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
		await message.answer("Выбери данные для изменения!", reply_markup=custom_moduls.admin.list_of_colums.changing)
		await Admin_FSM.type_set.set()
	else:
		await message.answer("Введи правильный номер аудитории!")


# Изменение преподавателя
async def teacher_set(callback: types.CallbackQuery, state=Admin_FSM.type_set):
	async with state.proxy() as data:
<<<<<<< HEAD
		data['data_option'] = callback.data
	result = a.select_info_subject(data['data_option'], "subject", data['callback'])
	await callback.message.answer(f"Введи ФИО преподавателя!\nПреподаватель курса сейчас {result}!")
=======
		data["data_option"] = callback.data
	result = a.select_info_subject(data["data_option"], "subject", data['callback'])
	await callback.message.answer(f"Введи ФИО преподавателя!\nПреподаватель курса сейчас {result[0]}!")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await Admin_FSM.teacher_it.set()


async def teacher_it(message: types.Message, state=Admin_FSM.teacher_it):
	async with state.proxy() as data:
		data["text"] = message.text
	if re.fullmatch(r'(\w{2,})+[ ]+(\w{2,})+[ ]+(\w{2,})', message.text):
		a.update_info(data['data_option'], message.text, data['callback'])
<<<<<<< HEAD
		result = a.select_info_subject(data['data_option'], "subject", data['callback'])
		await message.answer(f"Ты изменил ФИО преподавателя! Курс будет проводить: {result}!")
=======
		result = a.select_info_subject(data["data_option"], "subject", data['callback'])
		await message.answer(f"Ты изменил ФИО преподавателя! Курс будет проводить: {result[0]}!")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
		await message.answer("Выбери данные для изменения!", reply_markup=custom_moduls.admin.list_of_colums.changing)
		await Admin_FSM.type_set.set()
	else:
		await message.answer("Введи правильное ФИО преподавателя!")


# Изменение комментария
async def comment_set(callback: types.CallbackQuery, state=Admin_FSM.type_set):
	async with state.proxy() as data:
<<<<<<< HEAD
		data['data_option'] = callback.data
	result = a.select_info_subject(data['data_option'], "subject", data['callback'])
	await callback.message.answer(f"Введи комметарий!\nКомментарий для курса сейчас: {result}!")
=======
		data["data_option"] = callback.data
	result = a.select_info_subject(data["data_option"], "subject", data['callback'])
	await callback.message.answer(f"Введи комметарий!\nКомментарий для курса сейчас: {result[0]}!")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await Admin_FSM.comment_it.set()


async def comment_it(message: types.Message, state=Admin_FSM.comment_it):
	async with state.proxy() as data:
		data["text"] = message.text
	a.update_info(data['data_option'], message.text, data['callback'])
<<<<<<< HEAD
	result = a.select_info_subject(data['data_option'], "subject", data['callback'])
	await message.answer(f"Ты изменил комментарий!\n{result}")
=======
	result = a.select_info_subject(data["data_option"], "subject", data['callback'])
	await message.answer(f"Ты изменил комментарий!\n{result[0]}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await message.answer("Выбери данные для изменения!", reply_markup=custom_moduls.admin.list_of_colums.changing)
	await Admin_FSM.type_set.set()


# Выбор статуса предмета
async def set_list(callback: types.CallbackQuery, state=Admin_FSM.set_subjects):
	async with state.proxy() as data:
		data['set_List'] = callback.data
	if data['set_List'] == 'open_butt':
<<<<<<< HEAD
		await callback.message.answer(f"Выберите предмет из списка <b>включенных</b>", reply_markup=a.gen_off_on_subject_but()["on"])
		await Admin_FSM.set_status_on.set()
		await callback.message.answer("Вернуться к выбору опции 👉🏻/back👈🏻")
	else:
		await callback.message.answer("Выберите предмет из списка <b>включенных</b>", reply_markup=a.gen_off_on_subject_but()["off"])
=======
		await callback.message.edit_text(f"Выберите предмет из списка <b>включенных</b>", reply_markup=a.gen_off_on_subject_but()["on"])
		await Admin_FSM.set_status_on.set()
		await callback.message.answer("Вернуться к выбору опции 👉🏻/back👈🏻")
	else:
		await callback.message.edit_text("Выберите предмет из списка <b>включенных</b>", reply_markup=a.gen_off_on_subject_but()["off"])
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
		await Admin_FSM.set_status_off.set()
		await callback.message.answer("Вернуться к выбору опции 👉🏻/back👈🏻")


async def set_status_on(callback: types.CallbackQuery, state=Admin_FSM.set_status_on):
	async with state.proxy() as data:
		data['subject_status'] = callback.data
<<<<<<< HEAD
	await callback.message.answer("Вы точно хотите включить\выключить курс?", reply_markup=KB.yes_no)
=======
	await callback.message.edit_text("Вы точно хотите включить\выключить курс?", reply_markup=KB.yes_no)
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await Admin_FSM.set_answer_on.set()


async def set_answer_on(callbck: types.CallbackQuery, state=Admin_FSM.set_answer_on):
	async with state.proxy() as data:
		data['answer'] = callbck.data
	if data['answer'] == 'ans_yes':
<<<<<<< HEAD
		a.update_subject_by_status('status', True, data['subject_status'])
		result = a.select_info_subject('status', 'subject', data['subject_status'])
		await callbck.message.answer(
=======
		a.update_info_status('status', True, data['subject_status'])
		result = a.select_info_subject('status', 'subject', data['subject_status'])
		await callbck.message.edit_text(
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
			f"Вы успешно изменили статус!\n Теперь статус предмета {data['subject_status']}: {result[0]}",
			reply_markup=a.gen_off_on_subject_but()["on"])
		await Admin_FSM.set_status_on.set()
		await callbck.message.answer("Вернуться к выбору опции 👉🏻/back👈🏻")
	else:
<<<<<<< HEAD
		a.update_subject_by_status('status', False, data['subject_status'])
		result = a.select_info_subject('status', 'subject', data['subject_status'])
		await callbck.message.answer(
=======
		a.update_info_status('status', False, data['subject_status'])
		result = a.select_info_subject('status', 'subject', data['subject_status'])
		await callbck.message.edit_text(
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
			f"Вы успешно изменили статус!\n Теперь статус предмета {data['subject_status']}: {result[0]}",
			reply_markup=a.gen_off_on_subject_but()["on"])
		await Admin_FSM.set_status_on.set()
		await callbck.message.answer("Вернуться к выбору опции 👉🏻/back👈🏻")


async def set_status_off(callback: types.CallbackQuery, state=Admin_FSM.set_status_off):
	async with state.proxy() as data:
		data['subject_status'] = callback.data
<<<<<<< HEAD
	await callback.message.answer("Вы точно хотите включить\выключить курс?", reply_markup=KB.yes_no)
=======
	await callback.message.edit_text("Вы точно хотите включить\выключить курс?", reply_markup=KB.yes_no)
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await Admin_FSM.set_answer_off.set()


async def set_answer_off(callbck: types.CallbackQuery, state=Admin_FSM.set_answer_off):
	async with state.proxy() as data:
		data['answer'] = callbck.data
	if data['answer'] == 'ans_yes':
<<<<<<< HEAD
		a.update_subject_by_status('status', True, data['subject_status'])
		result = a.select_info_subject('status', 'subject', data['subject_status'])
		await callbck.message.answer(f"Вы успешно изменили статус!\n Теперь статус предмета {data['subject_status']}: {result[0]}",reply_markup=a.gen_off_on_subject_but()["off"])
		await Admin_FSM.set_status_off.set()
		await callbck.message.answer("Вернуться к выбору опции 👉🏻/back👈🏻")
	else:
		a.update_subject_by_status('status', False, data['subject_status'])
		result = a.select_info_subject('status', 'subject', data['subject_status'])
		await callbck.message.answer(f"Вы успешно изменили статус!\n Теперь статус предмета {data['subject_status']}: {result[0]}",reply_markup=a.gen_off_on_subject_but()["off"])
		await Admin_FSM.set_status_off.set()
		await callbck.message.answer("Вернуться к выбору опции 👉🏻/back👈🏻")

#возвращение домой
async def reg_as_stud(callback: types.CallbackQuery, state= Admin_FSM.cheking_data):
	result = a.join_select_info_users(callback.from_user.id)
	if result:
		await callback.message.answer("Приветствую вас вновь!", reply_markup=KB.stud_button)
		await User_FSM.main_buttons.set()
	else:
		await callback.message.edit_text("Вы не регистрировались? Исправьте эту ошибку!")
		await callback.message.answer("Укажите свое ФИО. Пример Сергей Сергеев Сергеевич")
		await User_FSM.registration.set()

=======
		a.update_info_status('status', True, data['subject_status'])
		result = a.select_info_subject('status', 'subject', data['subject_status'])
		await callbck.message.edit_text(f"Вы успешно изменили статус!\n Теперь статус предмета {data['subject_status']}: {result[0]}",reply_markup=a.gen_off_on_subject_but()["off"])
		await Admin_FSM.set_status_off.set()
		await callbck.message.answer("Вернуться к выбору опции 👉🏻/back👈🏻")
	else:
		a.update_info_status('status', False, data['subject_status'])
		result = a.select_info_subject('status', 'subject', data['subject_status'])
		await callbck.message.edit_text(f"Вы успешно изменили статус!\n Теперь статус предмета {data['subject_status']}: {result[0]}",reply_markup=a.gen_off_on_subject_but()["off"])
		await Admin_FSM.set_status_off.set()
		await callbck.message.answer("Вернуться к выбору опции 👉🏻/back👈🏻")

>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339

def admin_hendlers():
	dp.register_message_handler(cmd_cancel, commands='cancel', state='*')
	dp.register_message_handler(back, commands='back', state=Admin_FSM.set_status_on)
	dp.register_message_handler(back, commands='back', state=Admin_FSM.set_status_off)
	dp.register_message_handler(menu, commands= 'menu', state=Admin_FSM.change_option)
	dp.register_message_handler(menu, commands= 'menu', state=Admin_FSM.set_subjects)
	dp.register_callback_query_handler(came_data, text='verification', state=Admin_FSM.catching_text)
	dp.register_message_handler(coming_text, state=Admin_FSM.cheking_data)
	dp.register_callback_query_handler(cours_type, state=Admin_FSM.course)
	dp.register_callback_query_handler(options, state=Admin_FSM.change_option)
	dp.register_callback_query_handler(cost_set, text='cost', state=Admin_FSM.type_set)
	dp.register_callback_query_handler(schedule_set, text='schedule', state=Admin_FSM.type_set)
	dp.register_callback_query_handler(room_set, text='room', state=Admin_FSM.type_set)
	dp.register_callback_query_handler(teacher_set, text='teacher', state=Admin_FSM.type_set)
	dp.register_callback_query_handler(comment_set, text='comment', state=Admin_FSM.type_set)
	dp.register_message_handler(cost_it, state=Admin_FSM.cost_it)
	dp.register_message_handler(schedule_it, state=Admin_FSM.schedule_it)
	dp.register_message_handler(room_it, state=Admin_FSM.room_it)
	dp.register_message_handler(teacher_it, state=Admin_FSM.teacher_it)
	dp.register_message_handler(comment_it, state=Admin_FSM.comment_it)
	dp.register_callback_query_handler(set_list, state=Admin_FSM.set_subjects)
	dp.register_callback_query_handler(set_status_on, state=Admin_FSM.set_status_on)
	dp.register_callback_query_handler(set_status_off, state=Admin_FSM.set_status_off)
	dp.register_callback_query_handler(set_answer_on, state=Admin_FSM.set_answer_on)
	dp.register_callback_query_handler(set_answer_off, state=Admin_FSM.set_answer_off)
<<<<<<< HEAD
	dp.register_callback_query_handler(reg_as_stud, text= 'stud', state=Admin_FSM.cheking_data)
=======
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
