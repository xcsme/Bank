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
            n = int(input("Выбрать: "))
            if n == 1:
                while True:
                    balance = int(input("Введите сумму: "))
                    if bank.balance(login, balance):
                        bank.update_balance(login, balance)
                        print("Возьмите деньги")
                        time.sleep(2)
                        print(f'ваш баланс {bank.get_balance(login)}')
                        break
                    else:
                        print('Недостаточно суммы на счету')
                        continue

            elif n == 2:
                balance_2=int(input("Введите сумму: "))

                bank.update_balance_2(login, balance_2)
                print("Успешно")
                time.sleep(2)
                print(f'Ваш баланс: {bank.get_balance(login)}')
            elif n == 3:
                print('Input password')
                password_old = input('Password old')
                while True:
                    if bank.auth_password(login,password_old):
                        print("Input new password")
                        new_password = input('New password')
                        if len(new_password) < 6:
                            continue
                        bank.update_password(login,new_password)
                        print("Пароль обновлен")
                        time.sleep(2)
                        break
        else:
            print('Пароль введен неправильно')
    else:
        print("Логин введен неправильно")