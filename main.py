from aiogram import executor
from Module import dp
import KB
import cfg
import Admin_FSM_line
from Admin_FSM_line import *

Admin_FSM_line.admin_hendlers()

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

async def on_startup(_):
	print("Ты меня запустил!")





@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
	await message.answer(cfg.role, reply_markup=KB.Menu)


@dp.callback_query_handler(text='admin')
async def check_admin_bd(callback: types.CallbackQuery):
	cursor.execute(f"""SELECT id FROM admin WHERE id = {callback.from_user.id} """)
	if cursor.fetchone():
		await callback.message.edit_text(cfg.admin_hello, reply_markup= KB.Option)
		await Admin_FSM.catching_text.set()
	else:
		await callback.message.answer(cfg.not_admin_hello)


@dp.callback_query_handler(text='stud')
async def check_stud_bd(callback: types.CallbackQuery):
	cursor.execute(f"""SELECT id FROM stud WHERE id = {callback.from_user.id}""")
	if cursor.fetchone():
		await callback.message.answer(cfg.stud_hello)
	else:
		await callback.message.answer(cfg.call_to_reg)



if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
