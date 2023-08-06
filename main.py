import custom_moduls.admin.admin_FSM_line
import custom_moduls.user.User_line
from custom_moduls.database.sqliteclass import Database
from aiogram import executor
from Module import *
from custom_moduls.admin.admin_FSM_line import Admin_FSM
from custom_moduls.user.User_line import User_FSM
import KB
custom_moduls.user.User_line.user_hendlers()
custom_moduls.admin.admin_FSM_line.admin_hendlers()

a = Database("Dolg_bot_bd")

async def on_startup(_):
	print("Ты меня запустил!")

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
	await message.answer("Здравствуй, Студент!", reply_markup= KB.Menu)

@dp.callback_query_handler(text= 'stud')
async def auntification(callback: types.CallbackQuery):
	result = a.join_select_info_users(callback.from_user.id)
	if result:
		await callback.message.answer("Приветствую вас вновь!", reply_markup= KB.stud_button)
		await User_FSM.main_buttons.set()
	else:
		await callback.message.edit_text("Вы не регистрировались? Исправьте эту ошибку!")
		await callback.message.answer("Укажите свое ФИО. Пример Сергей Сергеев Сергеевич")
		await User_FSM.registration.set()

@dp.message_handler(commands=['admin'], state= '*')
async def check_admin_bd(message: types.Message):
	result = a.join_select_info_admin(message.from_user.id)
	if result:
		await message.answer("приветствую вас!\nВыберите шаг!", reply_markup=KB.Option)
		await Admin_FSM.catching_text.set()
	else:
		await message.answer("Вы не являетесь админом, приветствую, Вас, студент!", reply_markup= KB.stud_button)
		await User_FSM.main_buttons.set()

if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup, skip_updates=True)