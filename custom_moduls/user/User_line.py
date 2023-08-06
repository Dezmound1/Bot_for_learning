from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import StatesGroup, State
from custom_moduls.database.sqliteclass import Database
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import *
from Module import dp, KB
import re
from datetime import datetime

a = Database("Dolg_bot_bd")

class User_FSM(StatesGroup):
	main_buttons= State()
	registration= State()
	group= State()
	number= State()
	date_birth= State()
	passport_number= State()
	passport_serial= State()
	passport_date= State()
	issued_by= State()
	division_code= State()
	residence= State()
	cours_whatch= State()
	info_watch= State()
	answer= State()
	remove_answer= State()
	remove_id= State()
	edit_user_info= State()
	user_message_name= State()
	user_message_group= State()
	user_message_phone= State()
	user_message_date= State()
	user_message_num_pass= State()
	user_message_serial_pass= State()
	user_message_issued_wthen= State()
	user_message_issued_by= State()
	user_message_code= State()
	user_message_reg= State()

async def cmd_cancel(message: types.Message, state= FSMContext):
	await state.finish()

async def cmd_menu(message: types.Message, state= User_FSM.cours_whatch):
	await message.answer("Вы вернулись в главное меню!", reply_markup= KB.stud_button)
	await User_FSM.main_buttons.set()

async def cmd_menu_my_cours(message: types.Message, state= User_FSM.remove_id):
	await message.answer("Вы вернулись в главное меню!", reply_markup= KB.stud_button)
	await User_FSM.main_buttons.set()

async def faq_contant(message: types.Message, state= User_FSM.main_buttons):
	await message.answer("Политика и частые вопросы.\nДля выбора других опций воспользуйтесь панелью", reply_markup= KB.faq_button)

async def faq_about(callback: types.CallbackQuery, state= User_FSM.main_buttons):
	await callback.message.edit_text("Это FAQ", reply_markup= KB.back_button)

async def politic(callback: types.CallbackQuery, state= User_FSM.main_buttons):
	await callback.message.edit_text("Это политика обработки ПДн", reply_markup=KB.back_button)

async def back_faq(callback: types.CallbackQuery, state= User_FSM.main_buttons):
	await callback.message.edit_text("Политика и частые вопросы.", reply_markup=KB.faq_button)

async def open_cours(message: types.Message, state= User_FSM.main_buttons):
	await message.answer("Вернуться назад /menu", reply_markup=ReplyKeyboardRemove())
	await message.answer("Открытые на данный момент курсы:", reply_markup=a.gen_off_on_subject_but()["on"])
	await User_FSM.cours_whatch.set()

# Работа с информацией по курсу
async def cours_whatch(callback: types.CallbackQuery, state= User_FSM.cours_whatch):
	async with state.proxy() as data:
		data["callback_cours"] = callback.data
<<<<<<< HEAD
	result = a.info_subject('title', data["callback_cours"])
=======
	result = a.info_subject('title', callback.data)
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await callback.message.edit_text(f"Предмет: {result}\nОзнакомтесь с информацией или запишитесь", reply_markup=KB.cours_info)
	await User_FSM.info_watch.set()

async def back_cours_whatch(callback: types.CallbackQuery, state= User_FSM.info_watch):
	async with state.proxy() as data:
		data["back_cours_whatch"] = callback.data
<<<<<<< HEAD
	result = a.info_subject('title', data["callback_cours"])
=======
	result = a.info_subject('title', callback.data)
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await callback.message.edit_text(f"Предмет: {result}\nОзнакомтесь с информацией или запишитесь", reply_markup=KB.cours_info)
	await User_FSM.info_watch.set()

async def load(callback: types.CallbackQuery, state= User_FSM.info_watch):
	async with state.proxy() as data:
		data["callback_load"] = callback.data
	if (int(data["callback_cours"]),) in a.info_reg(callback.from_user.id):
		await callback.message.edit_text("❌Вы <b>уже записывались</b> на этот курс, выберите другой❌\nВернуться назад /menu", reply_markup=a.gen_off_on_subject_but()["on"])
		await User_FSM.cours_whatch.set()
	else:
		await callback.message.edit_text("Вы уверены, что хотите записаться на курс?", reply_markup=KB.answer)
		await User_FSM.answer.set()

async def answer_yes(callback: types.CallbackQuery, state= User_FSM.answer):
	async with state.proxy() as data:
		data["answer"] = callback.data
	a.subject_id_into_array('array_append', data["callback_cours"], callback.from_user.id)
<<<<<<< HEAD
	result = a.info_subject('title', data["callback_cours"])
=======
	result = a.info_subject('title', callback.data)
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await callback.message.edit_text(f"✅Вы успешно записались на курс✅ {result}\nВернуться назад /menu", reply_markup=a.gen_off_on_subject_but()["on"])
	await User_FSM.cours_whatch.set()

async def answer_no(callback: types.CallbackQuery, state= User_FSM.answer):
	async with state.proxy() as data:
		data["answer"] = callback.data
	result = a.info_subject('title', data["callback_cours"])
	await callback.message.edit_text(f"Предмет: {result}\nОзнакомтесь с информацией или запишитесь", reply_markup=KB.cours_info)
<<<<<<< HEAD
	await User_FSM.info_watch.set()

async def cost(callback: types.CallbackQuery, state= User_FSM.info_watch):
	async with state.proxy() as data:
		data["type_info"] = callback.data
	result = a.info_subject('cost', data["callback_cours"])
	await callback.message.edit_text(f"стоимость курса: {result} рублей", reply_markup= KB.return_info)

async def schedule(callback: types.CallbackQuery, state= User_FSM.info_watch):
	async with state.proxy() as data:
		data["type_info"] = callback.data
	result = a.info_subject('schedule', data["callback_cours"])
	await callback.message.edit_text(f"курс проведется: {result} ", reply_markup= KB.return_info)

async def room(callback: types.CallbackQuery, state= User_FSM.info_watch):
	async with state.proxy() as data:
		data["type_info"] = callback.data
	result = a.info_subject('room', data["callback_cours"])
	await callback.message.edit_text(f"курс проведется в аудитории №{result}", reply_markup= KB.return_info)

async def teacher(callback: types.CallbackQuery, state= User_FSM.info_watch):
	async with state.proxy() as data:
		data["type_info"] = callback.data
	result = a.info_subject('teacher', data["callback_cours"])
	await callback.message.edit_text(f"курс проведет {result}", reply_markup= KB.return_info)

async def comment(callback: types.CallbackQuery, state= User_FSM.info_watch):
	async with state.proxy() as data:
		data["type_info"] = callback.data
	result = a.info_subject('comment', data["callback_cours"])
=======
	await User_FSM.cours_whatch.set()

async def cost(callback: types.CallbackQuery, state= User_FSM.info_watch):
	result = a.info_subject('cost', callback.data)
	await callback.message.edit_text(f"стоимость курса: {result} рублей", reply_markup= KB.return_info)

async def schedule(callback: types.CallbackQuery, state= User_FSM.info_watch):
	result = a.info_subject('schedule', callback.data)
	await callback.message.edit_text(f"курс проведется: {result} ", reply_markup= KB.return_info)

async def room(callback: types.CallbackQuery, state= User_FSM.info_watch):
	result = a.info_subject('room', callback.data)
	await callback.message.edit_text(f"курс проведется в аудитории №{result}", reply_markup= KB.return_info)

async def teacher(callback: types.CallbackQuery, state= User_FSM.info_watch):
	result = a.info_subject('teacher', callback.data)
	await callback.message.edit_text(f"курс проведет {result}", reply_markup= KB.return_info)

async def comment(callback: types.CallbackQuery, state= User_FSM.info_watch):
	result = a.info_subject('comment', callback.data)
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await callback.message.edit_text(f"{result}", reply_markup= KB.return_info)

async def back_list(callback: types.CallbackQuery, state= User_FSM.info_watch):
	await callback.message.edit_text(f"Открытые на данный момент курсы:", reply_markup=a.gen_off_on_subject_but()["on"])
	await User_FSM.cours_whatch.set()

async def my_cours(message: types.Message, state= User_FSM.main_buttons):
	if a.find_cours_user(message.from_user.id) != None:
		await message.answer("Вернуться назад /menu", reply_markup=ReplyKeyboardRemove())
		await message.answer("Ваши курсы", reply_markup=a.make_buttons_users(a.select_own_subjects_users(message.from_user.id)[0]))
		await User_FSM.remove_id.set()
	else:
		await message.answer("Ты еще не записывался на курсы")

async def remove_id_subject(callback: types.CallbackQuery, state= User_FSM.remove_id):
	async with state.proxy() as data:
		data["callback_remove_id"] = callback.data
	await callback.message.edit_text("вы уверены, что хотите отписаться от курса ?", reply_markup=KB.answer)
	await User_FSM.remove_answer.set()

async def remove_yes(callback: types.CallbackQuery, state= User_FSM.remove_id):
	async with state.proxy() as data:
		data["remove_yes"] = callback.data
	a.subject_id_into_array('array_remove', data["callback_remove_id"], callback.from_user.id)
	await callback.message.edit_text("✅Вы успешно отменили запись!✅", reply_markup=a.make_buttons_users(a.select_own_subjects_users(callback.from_user.id)[0]))
	await User_FSM.remove_id.set()

async def remove_no(callback: types.CallbackQuery, state= User_FSM.remove_id):
	await callback.message.edit_text("Ваши курсы\nДля выбора других опций воспользуйтесь панелью", reply_markup=a.make_buttons_users(a.select_own_subjects_users(callback.from_user.id)[0]))
	await User_FSM.remove_id.set()

async def my_data(message: types.Message, state= User_FSM.main_buttons):
	await message.answer("Ваши личные данные", reply_markup= KB.about_user_buttons)
	await User_FSM.edit_user_info.set()


async def back(message: types.Message, state= User_FSM.main_buttons):
	await message.answer("Приветствую вас вновь!", reply_markup= KB.stud_button)

#РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ
async def full_name(message: types.Message, state= User_FSM.registration):
	async with state.proxy() as data:
		data["full_name"] = message.text
	answer = re.fullmatch(r'(\w{2,})+[ ]+(\w{2,})+[ ]+(\w{2,})', message.text)  # ФИО
	if answer:
<<<<<<< HEAD
		await message.answer("Введи название своей группы. Пример: БИС-21-1")
=======
		await message.answer("Введи название своей группы")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
		await User_FSM.group.set()
	else:
		await message.answer("Введи корректное ФИО")

async def group(message: types.Message, state= User_FSM.group):
	async with state.proxy() as data:
		data["group"] = message.text
	answer = re.search(r'(\S)+[-]+(\d{2})', message.text)
	if answer:
<<<<<<< HEAD
		await message.answer("Введи номер телефона. Пример: +79991111111 или 89991111111")
=======
		await message.answer("Введи номер телефона")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
		await User_FSM.number.set()
	else:
		await message.answer("Введи корректное название!")

async def number(message: types.Message, state= User_FSM.number):
	async with state.proxy() as data:
		data["number"] = message.text
	answer = re.fullmatch(r'(([+]+79)|89)+\d{9}', message.text)
	if answer:
<<<<<<< HEAD
		await message.answer("Введи дату рождения. Пример: 31.12.2000 Год не ниже 2000")
		await User_FSM.date_birth.set()
	else:
		await message.answer("Введи номер правильно")
=======
		await message.answer("Введи дату рождения")
		await User_FSM.date_birth.set()
	else:
		await message.answer("Введи корректо дату")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339

async def date_birth(message: types.Message, state= User_FSM.date_birth):
	async with state.proxy() as data:
		data["date_bith"] = message.text
	answer = re.fullmatch(r'(([0-2][1-9])|3+[0-1])+[.]+((0+[1-9])|[10-12])+[.]+(200+[0-8])', message.text)
	if answer:
<<<<<<< HEAD
		await message.answer("Введите серию паспорта. Пример: 123456")
		await User_FSM.passport_number.set()
	else:
		await message.answer("Введите корректно дату рождения. Год не ниже 2000")
=======
		await message.answer("Введите номер паспорта")
		await User_FSM.passport_number.set()
	else:
		await message.answer("Введите корректно дату рождения")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339

async def passport_num(message: types.Message, state= User_FSM.passport_number):
	async with state.proxy() as data:
		data["pass_num"] = message.text
	answer = re.fullmatch(r'\d{6}', message.text)
	if answer:
<<<<<<< HEAD
		await message.answer("введи номер паспорта. Пример: 1234")
		await User_FSM.passport_serial.set()
	else:
		await message.answer("введи серию паспорта правильно")
=======
		await message.answer("введи серию паспорта")
		await User_FSM.passport_serial.set()
	else:
		await message.answer("введи номер паспорта правильно")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339

async def passport_serial(message: types.Message, state= User_FSM.passport_serial):
	async with state.proxy() as data:
		data["pass_serial"] = message.text
	answer = re.fullmatch(r'\d{4}', message.text)
	if answer:
<<<<<<< HEAD
		await message.answer("Укажи, дату выдачи паспорта. Пример: 31.08.2015 Год не ниже 2015")
		await User_FSM.passport_date.set()
	else:
		await message.answer("Неправильно введен номер")
=======
		await message.answer("Укажи, дату выдачи паспорта")
		await User_FSM.passport_date.set()
	else:
		await message.answer("Неправильно введена дата")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339

async def passport_date(message: types.Message, state= User_FSM.passport_date):
	async with state.proxy() as data:
		data["pass_date"] = message.text
	answer = re.fullmatch(r'(([0-2][1-9])|3+[0-1])+[.]+((0+[1-9])|[10-12])+[.]+((201+[5-9])|(202+[0-5]))', message.text)
	if answer:
		await message.answer("Укажи кем выдан паспорт")
		await User_FSM.issued_by.set()
	else:
<<<<<<< HEAD
		await message.answer("Введи правельную дату. Год не ниже 2015")
=======
		await message.answer("Введи правельную дату")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339

async def issued_by(message: types.Message, state= User_FSM.issued_by):
	async with state.proxy() as data:
		data["issued_by"] = message.text
<<<<<<< HEAD
	await message.answer("Введи код подразделения. Пример: 123-123")
=======
	await message.answer("Введи код подразделения")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.division_code.set()

async def division_code(message: types.Message, state= User_FSM.division_code):
	async with state.proxy() as data:
		data["code"] = message.text
	answer = re.fullmatch(r'(\d{3})+[-]+(\d{3})', message.text)
	if answer:
		await message.answer("Введи место прописки")
		await User_FSM.residence.set()
	else:
		await message.answer("Неверный код подразделения")

async def residence(message: types.Message, state= User_FSM.residence):
	async with state.proxy() as data:
		data["residence"] = message.text
	await message.answer("Благодарим за регистрацию!", reply_markup=KB.stud_button)
	await User_FSM.main_buttons.set()
	# Форматирование дат под нормы pastgresql
<<<<<<< HEAD
	def formated_date(date):
		day, month, year = date.split(".")
		formatted_date = f"{year}.{month.zfill(2)}.{day.zfill(2)}"
		return formatted_date
	# Инсерт данных в БД users и passport
	user_id = a.insert_data_users(message.from_user.id, data["full_name"], data["group"], data["number"], formated_date(data["date_bith"]))
	a.insert_data_passport(user_id, formated_date(data["pass_date"]), data["issued_by"], data["code"], data["residence"], data["pass_num"], data["pass_serial"])
=======
	date_birth_obj= datetime.strptime(data["date_bith"], "%d.%m.%Y")
	pass_date_obj= datetime.strptime(data["pass_date"], "%d.%m.%Y")
	formatted_date_birth=  date_birth_obj.strftime("%Y.%m.%d")
	formatted_pass_date=  pass_date_obj.strftime("%Y.%m.%d")
	# Инсерт данных в БД users и passport
	user_id = a.insert_data_users(message.from_user.id, data["full_name"], data["group"], data["number"], formatted_date_birth)
	a.insert_data_passport(user_id, formatted_pass_date, data["issued_by"], data["code"], data["residence"], data["pass_num"], data["pass_serial"])
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339

# Обновление данных в личном кабинете
async def user_name(message: types.Message, state= User_FSM.edit_user_info):
	async with state.proxy() as data:
		data["user_name"] = message.text
	result = a.select_info_users('users', 'full_name', message.from_user.id)
<<<<<<< HEAD
	await message.answer(f"Ваше ФИО: {result}\nИзмените")
=======
	await message.answer(f"Ваше ФИО: {result}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.user_message_name.set()

async def user_message_name(message: types.Message, state= User_FSM.user_message_name):
	async with state.proxy() as data:
		data["user_message_name"] = message.text
	answer = re.fullmatch(r'(\w{2,})+[ ]+(\w{2,})+[ ]+(\w{2,})', message.text)  # ФИО
	if answer:
		a.update_data_users('users', 'full_name', data["user_message_name"], message.from_user.id)
		await message.answer("✅Вы успешно изменили данные✅\nВыберите другие параметры или вернитесь в главное меню", reply_markup=KB.about_user_buttons)
		await User_FSM.edit_user_info.set()
	else:
		await message.answer("❌Введите правельно данные❌")

async def user_group(message: types.Message, state= User_FSM.edit_user_info):
	async with state.proxy() as data:
		data["user_group"] = message.text
	result = a.select_info_users('users', 'group_name', message.from_user.id)
<<<<<<< HEAD
	await message.answer(f"Ваша группа: {result}\nИзмените")
=======
	await message.answer(f"Ваша группа: {result}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.user_message_group.set()

async def user_message_group(message: types.Message, state= User_FSM.user_message_group):
	async with state.proxy() as data:
		data["user_message_group"] = message.text
	answer = re.search(r'(\S)+[-]+(\d{2})', message.text)  # группа
	if answer:
		a.update_data_users('users', 'group_name', data["user_message_group"], message.from_user.id)
		await message.answer("✅Вы успешно изменили данные✅\nВыберите другие параметры или вернитесь в главное меню", reply_markup=KB.about_user_buttons)
		await User_FSM.edit_user_info.set()
	else:
		await message.answer("❌Введите правильно данные❌")

async def user_phone(message: types.Message, state= User_FSM.edit_user_info):
	async with state.proxy() as data:
		data["user_phone"] = message.text
	result = a.select_info_users('users', 'phone_number', message.from_user.id)
<<<<<<< HEAD
	await message.answer(f"Ваш номер телефона: {result}\nИзмените")
=======
	await message.answer(f"Ваш номер телефона: {result}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.user_message_phone.set()

async def user_message_phone(message: types.Message, state= User_FSM.user_message_phone):
	async with state.proxy() as data:
		data["user_message_phone"] = message.text
	answer = re.fullmatch(r'(([+]+79)|89)+\d{9}', message.text)# номер телефона
	if answer:
		a.update_data_users('users', 'phone_number', data["user_message_phone"], message.from_user.id)
		await message.answer("✅Вы успешно изменили данные✅\nВыберите другие параметры или вернитесь в главное меню", reply_markup=KB.about_user_buttons)
		await User_FSM.edit_user_info.set()
	else:
		await message.answer("❌Введите правельно данные❌")

async def user_date_update(message: types.Message, state= User_FSM.edit_user_info):
	async with state.proxy() as data:
		data["user_date_update"] = message.text
	result = a.select_info_users('users', 'date_birth', message.from_user.id)
<<<<<<< HEAD
	await message.answer(f"Ваша дата: {result}\nИзмените")
=======
	await message.answer(f"Ваша дата: {result}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.user_message_date.set()

async def user_message_date(message: types.Message, state= User_FSM.user_message_date):
	async with state.proxy() as data:
		data["user_message_date"] = message.text
	answer = re.fullmatch(r'(([0-2][1-9])|3+[0-1])+[.]+((0+[1-9])|[10-12])+[.]+(200+[0-8])', message.text)  # группа
	if answer:
		a.update_data_users('users', 'date_birth', data["user_message_date"], message.from_user.id)
		await message.answer("✅Вы успешно изменили данные✅\nВыберите другие параметры или вернитесь в главное меню", reply_markup=KB.about_user_buttons)
		await User_FSM.edit_user_info.set()
	else:
		await message.answer("❌Введите правельно данные❌")

async def user_num_pass(message: types.Message, state= User_FSM.edit_user_info):
	async with state.proxy() as data:
		data["user_num_pass"] = message.text
	result = a.select_passport_by_telegram_id(message.from_user.id, 'number')
<<<<<<< HEAD
	await message.answer(f"Ваш серию паспорта: {result}\nИзмените")
=======
	await message.answer(f"Ваш номер паспорта: {result}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.user_message_num_pass.set()

async def user_message_num_pass(message: types.Message, state= User_FSM.user_message_num_pass):
	async with state.proxy() as data:
		data["user_message_num_pass"] = message.text
<<<<<<< HEAD
	answer = re.fullmatch(r'\d{4}', message.text)  # группа
=======
	answer = re.fullmatch(r'\d{6}', message.text)  # группа
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	if answer:
		a.update_passport_issued_date_by_telegram_id(message.from_user.id, 'number', data["user_message_num_pass"])
		await message.answer("✅Вы успешно изменили данные✅\nВыберите другие параметры или вернитесь в главное меню", reply_markup=KB.about_user_buttons)
		await User_FSM.edit_user_info.set()
	else:
		await message.answer("❌Введите правельно данные❌")

async def user_serial_pas(message: types.Message, state= User_FSM.edit_user_info):
	async with state.proxy() as data:
		data["user_serial_pas"] = message.text
	result = a.select_passport_by_telegram_id(message.from_user.id, 'serial')
<<<<<<< HEAD
	await message.answer(f"Ваш номер паспорта: {result}\nИзмените")
=======
	await message.answer(f"Ваш серию паспорта: {result}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.user_message_serial_pass.set()

async def user_message_serial_pass(message: types.Message, state= User_FSM.user_message_serial_pass):
	async with state.proxy() as data:
		data["user_message_serial_pass"] = message.text
<<<<<<< HEAD
	answer = re.fullmatch(r'\d{6}', message.text)  # группа
=======
	answer = re.fullmatch(r'\d{4}', message.text)  # группа
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	if answer:
		a.update_passport_issued_date_by_telegram_id(message.from_user.id, 'serial', data["user_message_serial_pass"])
		await message.answer("✅Вы успешно изменили данные✅\nВыберите другие параметры или вернитесь в главное меню", reply_markup=KB.about_user_buttons)
		await User_FSM.edit_user_info.set()
	else:
		await message.answer("❌Введите правельно данные❌")

async def user_issued_wthen(message: types.Message, state= User_FSM.edit_user_info):
	async with state.proxy() as data:
		data["user_issued_wthen"] = message.text
	result = a.select_passport_by_telegram_id(message.from_user.id, 'issued_date')
<<<<<<< HEAD
	await message.answer(f"паспорт выдан : {result}\nИзмените")
=======
	await message.answer(f"паспорт выдан : {result}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.user_message_issued_wthen.set()

async def user_message_issued_wthen(message: types.Message, state= User_FSM.user_message_issued_wthen):
	async with state.proxy() as data:
		data["user_message_issued_wthen"] = message.text
	answer = re.fullmatch(r'(([0-2][1-9])|3+[0-1])+[.]+((0+[1-9])|[10-12])+[.]+((201+[5-9])|(202+[0-5]))', message.text) # выдан кем
	if answer:
		a.update_passport_issued_date_by_telegram_id(message.from_user.id, 'issued_date', data["user_message_issued_wthen"])
		await message.answer("✅Вы успешно изменили данные✅\nВыберите другие параметры или вернитесь в главное меню", reply_markup=KB.about_user_buttons)
		await User_FSM.edit_user_info.set()
	else:
		await message.answer("❌Введите правельно данные❌")

async def user_issued_by(message: types.Message, state= User_FSM.edit_user_info):
	async with state.proxy() as data:
		data["user_issued_by"] = message.text
	result = a.select_passport_by_telegram_id(message.from_user.id, 'issued_by')
<<<<<<< HEAD
	await message.answer(f"паспорт выдан: {result}\nИзмените")
=======
	await message.answer(f"паспорт выдан: {result}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.user_message_issued_by.set()

async def user_message_issued_by(message: types.Message, state= User_FSM.user_message_issued_by):
	async with state.proxy() as data:
		data["user_message_issued_by"] = message.text
		a.update_passport_issued_date_by_telegram_id(message.from_user.id, 'issued_by', data["user_message_issued_by"])
		await message.answer("✅Вы успешно изменили данные✅\nВыберите другие параметры или вернитесь в главное меню", reply_markup=KB.about_user_buttons)
		await User_FSM.edit_user_info.set()

async def user_code(message: types.Message, state= User_FSM.edit_user_info):
	async with state.proxy() as data:
		data["user_code"] = message.text
	result = a.select_passport_by_telegram_id(message.from_user.id, 'division_code')
<<<<<<< HEAD
	await message.answer(f"Код регистрации: {result}\nИзмените")
=======
	await message.answer(f"Код регистрации: {result}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.user_message_code.set()

async def user_message_code(message: types.Message, state= User_FSM.user_message_code):
	async with state.proxy() as data:
		data["user_message_code"] = message.text
	answer = re.fullmatch(r'(\d{3})+[-]+(\d{3})', message.text)  # код
	if answer:
		a.update_passport_issued_date_by_telegram_id(message.from_user.id, 'division_code', data["user_message_code"])
		await message.answer("✅Вы успешно изменили данные✅\nВыберите другие параметры или вернитесь в главное меню", reply_markup=KB.about_user_buttons)
		await User_FSM.edit_user_info.set()
	else:
		await message.answer("❌Введите правельно данные❌")

async def user_reg(message: types.Message, state= User_FSM.edit_user_info):
	async with state.proxy() as data:
		data["user_reg"] = message.text
	result = a.select_passport_by_telegram_id(message.from_user.id, 'residence')
<<<<<<< HEAD
	await message.answer(f"Место регистрации: {result}\nИзмените")
=======
	await message.answer(f"Место регистрации: {result}")
>>>>>>> d1e4d78f11005b874321d6c9f8c1f206c8ba8339
	await User_FSM.user_message_reg.set()

async def user_message_reg(message: types.Message, state= User_FSM.user_message_reg):
	async with state.proxy() as data:
		data["user_message_reg"] = message.text
		a.update_passport_issued_date_by_telegram_id(message.from_user.id, 'residence', data["user_message_reg"])
		await message.answer("✅Вы успешно изменили данные✅\nВыберите другие параметры или вернитесь в главное меню", reply_markup=KB.about_user_buttons)
		await User_FSM.edit_user_info.set()

async def back_menu(message: types.Message, state= User_FSM.edit_user_info):
	await message.answer("Вы вернулись в главное меню!", reply_markup=KB.stud_button)
	await User_FSM.main_buttons.set()

def user_hendlers():
	dp.register_message_handler(cmd_cancel, commands='cancel', state='*')
	dp.register_message_handler(cmd_menu, commands='menu', state= User_FSM.cours_whatch)
	dp.register_message_handler(cmd_menu_my_cours, commands='menu', state=User_FSM.remove_id)
	dp.register_message_handler(faq_contant, text='FAQ', state=User_FSM.main_buttons)
	dp.register_message_handler(open_cours, text='Открытые курсы', state=User_FSM.main_buttons)
	dp.register_message_handler(my_cours, text='Мои курсы', state=User_FSM.main_buttons)
	dp.register_message_handler(my_data, text='Личные данные', state=User_FSM.main_buttons)
	dp.register_message_handler(back, text='Назад', state=User_FSM.main_buttons)
	dp.register_callback_query_handler(back_faq, text='back_faq', state=User_FSM.main_buttons)
	dp.register_callback_query_handler(faq_about, text='about', state=User_FSM.main_buttons)
	dp.register_callback_query_handler(politic, text='politic', state=User_FSM.main_buttons)
	dp.register_message_handler(full_name, state=User_FSM.registration)
	dp.register_message_handler(group, state= User_FSM.group)
	dp.register_message_handler(number, state= User_FSM.number)
	dp.register_message_handler(date_birth, state= User_FSM.date_birth)
	dp.register_message_handler(passport_num, state= User_FSM.passport_number)
	dp.register_message_handler(passport_serial, state=User_FSM.passport_serial)
	dp.register_message_handler(passport_date, state=User_FSM.passport_date)
	dp.register_message_handler(issued_by, state=User_FSM.issued_by)
	dp.register_message_handler(division_code, state=User_FSM.division_code)
	dp.register_message_handler(residence, state=User_FSM.residence)
	dp.register_callback_query_handler(back_faq, text='back_faq', state=User_FSM.main_buttons)
	dp.register_callback_query_handler(cours_whatch, state= User_FSM.cours_whatch)
	dp.register_callback_query_handler(cost, text= 'cost', state=User_FSM.info_watch)
	dp.register_callback_query_handler(schedule, text = 'schedule', state = User_FSM.info_watch)
	dp.register_callback_query_handler(room, text = 'room', state = User_FSM.info_watch)
	dp.register_callback_query_handler(teacher, text = 'teacher', state = User_FSM.info_watch)
	dp.register_callback_query_handler(comment, text = 'comment', state = User_FSM.info_watch)
	dp.register_callback_query_handler(back_list, text = 'back_list', state = User_FSM.info_watch)
	dp.register_callback_query_handler(back_cours_whatch, text='return_info', state=User_FSM.info_watch)
	dp.register_callback_query_handler(load, text='load', state=User_FSM.info_watch)
	dp.register_callback_query_handler(answer_yes, text='yes', state=User_FSM.answer)
	dp.register_callback_query_handler(answer_no, text='no', state=User_FSM.answer)
	dp.register_callback_query_handler(remove_id_subject, state=User_FSM.remove_id)
	dp.register_callback_query_handler(remove_yes, text='yes', state=User_FSM.remove_answer)
	dp.register_callback_query_handler(remove_no, text='no', state=User_FSM.remove_answer)
	dp.register_message_handler(user_name, text='ФИО', state=User_FSM.edit_user_info)
	dp.register_message_handler(user_group, text='Группа', state=User_FSM.edit_user_info)
	dp.register_message_handler(user_phone, text='Номер телефона', state=User_FSM.edit_user_info)
	dp.register_message_handler(user_date_update, text='Дата рождения', state=User_FSM.edit_user_info)
	dp.register_message_handler(user_num_pass, text='Номер паспорта', state=User_FSM.edit_user_info)
	dp.register_message_handler(user_serial_pas, text='Серия паспорта', state=User_FSM.edit_user_info)
	dp.register_message_handler(user_issued_wthen, text='Дата выдачи', state=User_FSM.edit_user_info)
	dp.register_message_handler(user_issued_by, text='Кем выдан', state=User_FSM.edit_user_info)
	dp.register_message_handler(user_code, text='Код подразделения', state=User_FSM.edit_user_info)
	dp.register_message_handler(user_reg, text='Место регистрации', state=User_FSM.edit_user_info)
	dp.register_message_handler(back_menu, text='Назад', state=User_FSM.edit_user_info)
	dp.register_message_handler(user_message_name, state=User_FSM.user_message_name)
	dp.register_message_handler(user_message_group, state=User_FSM.user_message_group)
	dp.register_message_handler(user_message_phone, state=User_FSM.user_message_phone)
	dp.register_message_handler(user_message_date, state=User_FSM.user_message_date)
	dp.register_message_handler(user_message_num_pass, state=User_FSM.user_message_num_pass)
	dp.register_message_handler(user_message_serial_pass, state=User_FSM.user_message_serial_pass)
	dp.register_message_handler(user_message_issued_wthen, state=User_FSM.user_message_issued_wthen)
	dp.register_message_handler(user_message_issued_by, state=User_FSM.user_message_issued_by)
	dp.register_message_handler(user_message_code, state=User_FSM.user_message_code)
	dp.register_message_handler(user_message_reg, state=User_FSM.user_message_reg)