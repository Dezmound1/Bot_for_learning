import os
import psycopg2
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Database:
	def __init__(self, db_name:str)-> None:
		self.db_name:str = db_name
		self.connection = psycopg2.connect(database=self.db_name, user="postgres", password="denchik2557204", host="localhost")
		self.cursor = self.connection.cursor()
		self.db_dir:str = ".\\"
		self.log_dir:str = os.path.join(self.db_dir, "log")
		self.log_admin:str = os.path.join(self.log_dir, "log_admin.txt")
		self.log_db:str = os.path.join(self.log_dir, "log_db.txt")

	def init_dir(self):
		if not os.path.exists(self.db_dir):
			os.mkdir(self.db_dir)
		if not os.path.exists(self.log_dir):
			os.mkdir(self.log_dir)

	def write_log(self, event:str, type_log:str)->None:
		try:
			if type_log == "admin":
				with open(self.log_admin, "a") as file:
					file.write(f"{event}\n")
			else:
				with open(self.log_db, "a") as file:
					file.write(f"{event}\n")
		except Exception as e:
			with open(self.log_db, "a") as file:
				file.write(f"{e}\n")

	def get_from_db(self, table_name:str)->list[tuple]:
		try:
			with self.connection:
				self.cursor.execute(f"SELECT * FROM {table_name}")
				return self.cursor.fetchall()
		except Exception as e:
			self.write_log(str(e), "db")

	def update_subject_by_status(self, colum:str, status:bool, subject_id:int):
		with self.connection:
			self.cursor.execute(f"""update subject set {colum} = {status} where id = {subject_id}""")
			self.connection.commit()

	def get_subjects_by_status(self, status:bool)->dict:
		with self.connection:
			self.cursor.execute("select id, title from subject where status = %s", (status,))
			return {key: value for key, value in self.cursor.fetchall()}

	def gen_off_on_subject_but(self)->dict:
		on_markapp:InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=1, resize_keyboard= True)
		on_markapp.add(*[InlineKeyboardButton(text=value,callback_data=key) for key, value in self.get_subjects_by_status(True).items()])

		off_markapp:InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=1, resize_keyboard= True)
		off_markapp.add(*[InlineKeyboardButton(text=value,callback_data=key) for key, value in self.get_subjects_by_status(False).items()])

		return {
			"off" : off_markapp,
			"on" : on_markapp
		}

	def get_pass(self, user_id:str)->str: #метод проверки пароля админов
		try:
			with self.connection:
				self.cursor.execute(f"""
					select 
						a.admin_password
					from admins a 
					join 
						users u on u.id = a.user_id 
					where u.telegram_id = {user_id}""")
				return self.cursor.fetchone()
		except Exception as e:
			self.write_log(str(e), "admin")

	def select_info_subject(self, colum:str, table_name:str, subject_id:int): #метод для отображения инфы сообщением от бота
		try:
			with self.connection:
				self.cursor.execute(f"""SELECT {colum} FROM {table_name} WHERE id = {subject_id}""")
				return self.cursor.fetchone()[0]
		except Exception as e:
			self.write_log(str(e), "db")

	def update_info(self, colum:str, message:str, id_subject:int)->None: #апдейт для аблицы subject
		try:
			with self.connection:
				self.cursor.execute(f"""UPDATE subject SET {colum} = '{message}' WHERE id = {id_subject} """)
				self.connection.commit()
		except Exception as e:
			self.write_log(str(e), "db")

	def join_select_info(self, telegram_callback_id):
		dict = {
			'admins':['admin_password'],
			'users':['telegram_id']
		}
		data = ', '.join([i[0]+'.'+j for i in dict.keys() for j in dict[i]])
		try:
			with self.connection:
				self.cursor.execute(f"select {data} from admins a join users u on u.id = a.users_id where u.telegram_id = {telegram_callback_id}")
		except Exception as e:
			self.write_log(str(e), "db")

	def join_select_info_admin(self, telegram_callback_id:str)->tuple:
		try:
			with self.connection:
				self.cursor.execute(f"""
					select
						u.telegram_id 
					from users u 
					join 
						admins a on u.id = a.user_id 
					where u.telegram_id = {telegram_callback_id}""")
				return self.cursor.fetchone()
		except Exception as e:
			self.write_log(str(e), "db")

	def join_select_info_users(self, telegram_callback_id:str):
		try:
			with self.connection:
				self.cursor.execute(f"select u.telegram_id from users u where u.telegram_id = {telegram_callback_id}")
				return self.cursor.fetchone()
		except Exception as e:
			self.write_log(str(e), "db")

	def select_own_subjects_users(self, telegram_message_id:int):# Получаем список айди предметов юзера
		try:
			with self.connection:
				self.cursor.execute(f"""
					select 
						u.array_subject_registration_id
					from users u
					where u.telegram_id = {telegram_message_id}
				""")
			return self.cursor.fetchone()
		except Exception as e:
			self.write_log(str(e), "db")

	def make_buttons_users(self, subjects_id:list):
		try:
			with self.connection:
				self.cursor.execute((f"""
					select
						s.id,
						s.title
					from subject s
					where s.id in %s
				"""), (tuple(subjects_id),))
			subject_dict= {row[0]:row[1] for row in self.cursor.fetchall()}
			on_markapp:InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
			on_markapp.add(*[InlineKeyboardButton(text=value, callback_data=key) for key, value in subject_dict.items()])
			return on_markapp
		except Exception as e:
			self.write_log(str(e), "db")

	def insert_data_users(self, telegram_id:int, full_name:str, group_name:str, phone_number, date_birth):
		try:
			with self.connection:
				self.cursor.execute(f"""
					insert into 
						users (telegram_id, full_name, group_name, phone_number, date_birth)
					values (%s, %s, %s, %s, %s)
					returning id;
				""", (telegram_id, full_name, group_name, phone_number, date_birth))
				self.connection.commit()
				user_id = self.cursor.fetchone()[0]
				return user_id
		except Exception as e:
			self.write_log(str(e), "db")

	def insert_data_passport(self, user_id, issued_date, issued_by:str, division_code, residence, number:int, serial):
		try:
			with self.connection:
				self.cursor.execute(f"""
					insert into 
						passport (user_id, issued_date, issued_by, division_code, residence, number, serial)
					values (%s, %s, %s, %s, %s, %s, %s)
				""", (user_id, issued_date, issued_by, division_code, residence, number, serial))
				self.connection.commit()
		except Exception as e:
			self.write_log(str(e), "db")

	def find_cours_user(self, user_id:int):
		try:
			with self.connection:
				self.cursor.execute(f"""
					select
						array_subject_registration_id
					from users
					where telegram_id = {user_id}
				""")
				return self.cursor.fetchone()[0]
		except Exception as e:
			self.write_log(str(e), "db")

	def info_subject(self, colum_name:str, callback_id:int):
		try:
			with self.connection:
				self.cursor.execute(f"""
					select
						{colum_name}
					from subject
					where id = {callback_id}
				""")
			return self.cursor.fetchone()[0]
		except Exception as e:
			self.write_log(str(e), "db")

	def info_reg(self, user_id:int):
		try:
			with self.connection:
				self.cursor.execute(f"""
					select 
						unnest(array_subject_registration_id)
					from users
					where telegram_id = {user_id}
			""")
			return self.cursor.fetchall()
		except Exception as e:
			self.write_log(str(e), "db")

	def subject_id_into_array(self, method:str, data:int, user_id:int):
		try:
			with self.connection:
				self.cursor.execute(f"""
		                UPDATE users
		                SET array_subject_registration_id = {method}(array_subject_registration_id, {data})
		                WHERE telegram_id = {user_id}
		    """)
		except Exception as e:
			self.write_log(str(e), "db")

	def select_info_users(self, table_name:str, data, user_id:int):
		try:
			with self.connection:
				self.cursor.execute(f"""
						select
							{data}
						from {table_name}
						where telegram_id = {user_id}
			""")
			return self.cursor.fetchone()[0]
		except Exception as e:
			self.write_log(str(e), "db")

	def update_data_users(self, table_name:str, colum:str, data, user_id:int):
		try:
			with self.connection:
				self.cursor.execute(f"""
						update
							{table_name}
						set {colum} = '{data}'
						where telegram_id = {user_id}
			""")
		except Exception as e:
			self.write_log(str(e), "db")

	def update_passport_issued_date_by_telegram_id(self, telegram_id: int, colum, issued_date: str):
		try:
			with self.connection:
				self.cursor.execute(f"""
	                SELECT id FROM users WHERE telegram_id = {telegram_id}
	            """)
				user_id = self.cursor.fetchone()
				if user_id is None:
					return
				user_id = user_id[0]
				self.cursor.execute(f"""
	                UPDATE passport
	                SET {colum} = '{issued_date}'
	                WHERE user_id = {user_id}
	            """)
		except Exception as e:
			self.write_log(str(e), "db")

	def update_subject_data_by_telegram_id(self, telegram_id: int, colum, data: str):
		try:
			with self.connection:
				self.cursor.execute(f"""
					select id from users where telegram_id = {telegram_id}
					
				""")
				user_id = self.cursor.fetchone()
				if user_id is None:
					return
				user_id = user_id[0]
				self.cursor.execute(f"""
					update subject
					set {colum} = '{data}'
					where user_id = {user_id}
				""")
		except Exception as e:
			self.write_log(str(e), "db")

	def select_passport_by_telegram_id(self, telegram_id:int, columns:str):
		try:
			with self.connection:
				self.cursor.execute(f"""
	                SELECT id FROM users WHERE telegram_id = {telegram_id}
	            """)
				user_id = self.cursor.fetchone()
				if user_id is None:
					return
				user_id = user_id[0]
				self.cursor.execute(f"""
	                SELECT {columns}
	                FROM passport
	                WHERE user_id = {user_id}
	            """)
				return self.cursor.fetchone()[0]
		except Exception as e:
			self.write_log(str(e), "db")
