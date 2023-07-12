import os
import sqlite3

class Database:
    def __init__(self):
        self.db_dir = "Classes"
        self.log_dir = os.path.join(self.db_dir, "log")
        self.log_file = os.path.join(self.log_dir, "log.txt")
        self.db_name = None
        self.table_name = None
        self.connection = None
        self.cursor = None
        self.cell = None

    def init_dir(self):
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)

    def write_log(self, event):
        with open(self.log_file, "a") as file:
            file.write(f"{event}\n")

    def init_db(self, name, table_name):
        self.db_name = name
        self.table_name = table_name
        db_path = os.path.join(self.db_dir, f"{self.db_name}.db")
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        if self.table_name == "users":
            self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY,
                full_name TEXT,
                group_name TEXT,
                phone_number INTEGER,
                date_of_birth TEXT,
                passport INTEGER,
                issued_by TEXT,
                division_code TEXT,
                address TEXT
            )''')
            self.connection.commit()
        elif self.table_name == "admin":
            self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name}(
                id INTEGER PRIMARY KEY,
                password TEXT
            )''')
            self.connection.commit()
        else:
            raise Exception("Таких БД не предполагалось.")

    def add_to_table_user(self, req):
        if not self.cursor:
            raise Exception("Database connection not initialized.")
        self.cursor.execute(f"INSERT INTO {self.table_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", req)
        self.connection.commit()

    def add_to_table_admin(self, value):
        self.velue = value
        if not self.cursor:
            raise Exception("Database connection not initialized.")
        self.cursor.execute(f"INSERT INTO {self.table_name} VALUES (?,?)", value)
        self.connection.commit()

    def get_from_db(self):
        if not self.cursor:
            raise Exception("Database connection not initialized.")
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.cursor.fetchall()


test = Database()
db = Database()
# test.init_db("tutorial", "admin")
# test.add_to_table_admin(("2674", "test"))
# db.init_dir()
# db.write_log("Кто-то сделал что-то")
db.init_db("example", "admin")
# db.add_to_table_user(("1234567","Динис", "БИС", "123456789", "2000-01-01", "1234567890", "ДВГТИ", "260-060", "Address"))
# data = db.get_from_db()
# print(data)



#проверка наличия таблици в бд через метотд чек дб
#если к ней можно подключться то ок
#коннект и курсор вывести в инициализацию класса
