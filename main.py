from bank import Bank
import time
bank = Bank('bank.db')
bank.create_table()

while True:
    #запросить у пользователя логин и пароль если есть в базе то запросить баланс
    login=input("Login: ")
    if bank.auth_login(login):
        password=input("Password: ")
        if bank.auth_password(login, password):
            print("Вход успешно выполнен")
            time.sleep(2)
            print("1 - снять\n2 - внести\n3 - изменить пароль")
            n = input("Enter")

        else:
            print('Пароль введен неправильно')
    else:
        print("Логин введен неправильно")