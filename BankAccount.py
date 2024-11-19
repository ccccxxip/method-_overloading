class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.set_balance(self.get_balance() + amount)

    def withdraw(self, amount):
        if amount > self.get_balance():
            raise ValueError("На счете недостаточно средств")
        elif amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        self.set_balance(self.get_balance() - amount)

    def transfer(self, account, amount):
        if amount > self.get_balance():
            raise ValueError("На счете недостаточно средств")
        elif amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")


        # Уменьшаем баланс текущего счета
        self.withdraw(amount)
        # Пополняем баланс указанного счета
        account.deposit(amount)

account1 = BankAccount(1000)
account2 = BankAccount()

print(account1.get_balance())  # Выведет 1000

account1.deposit(500)
print(account1.get_balance())  # Выведет 1500

try:
    account1.transfer(account2, 2000)
except ValueError as e:
    print(e)  # На счете недостаточно средств

account1.transfer(account2, 500)

print(account1.get_balance())  # Выведет 1000
print(account2.get_balance())  # Второй счет получит 500
