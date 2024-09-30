from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            x = randint(50, 501)
            self.balance += x
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {x}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            x = randint(50, 501)
            print(f"Запрос на {x}")
            if self.balance >= x:
                self.balance -= x
                print(f"Снятие: {x}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bank = Bank(0)
th1 = Thread(target=Bank.deposit, args=(bank,))
th2 = Thread(target=Bank.take, args=(bank,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bank.balance}')