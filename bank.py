import sqlite3
import random
class Bank:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS USERS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        LOGIN VARCHAR(255) NOT NULL,
        PASSWORD VARCHAR(255) NOT NULL,
        CASH INTEGER NOT NULL
         )''')
        #self.con.commit()
    def auth_login(self, login):
        self.cursor.execute('select * from users where login=?', (login,))
        if self.cursor.fetchall():
            return True
        return False

    def generate_users(self):
        for user in range(1, 101):
            self.cursor.execute('insert into users (login, password, cash) values(?,?,?)', ('user'+str(user), self.generate_password(), self.generate_cash()))
            self.con.commit()

    def generate_password(self):
        pass_s = 'fsdfglkwlaskflaskf2424@3$adfgasfadfgg45645747ukyu'
        password = ''
        for i in range(5):
            password += pass_s[random.randint(0, len(pass_s) - 1)]
        return password

    def generate_cash(self):
        return random.randint(1000, 10000)

    def auth_password(self, login, password):
        self.cursor.execute('select * from users where login = ? and password=?', (login, password,))
        if self.cursor.fetchall():
            return True
        return False

    def balance(self, login, cash):
        self.cursor.execute('select * from users where login=? and cash>=?', (login, cash))
        if self.cursor.fetchall():
            return True
        return False
    def update_balance(self, login, cash):
        self.cursor.execute('update users set cash=cash-? where login=?', (cash, login))
        self.con.commit()

    def get_balance(self, login):
        self.cursor.execute('select cash from users where login=?', (login,))
        return self.cursor.fetchone()[0]

    def update_balance_2(self, login, cash):
        self.cursor.execute('update users set cash=cash+? where login=?', (cash, login))
        self.con.commit()

    def update_password(self, login, password):
        print(login, password)
        self.cursor.execute('update users set password=? where login=?', (password, login, ))
        self.con.commit()
