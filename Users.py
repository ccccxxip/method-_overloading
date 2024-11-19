class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not new_name.isalpha():
            raise ValueError("Некорректное имя")
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or not (0 <= new_age <= 110):
            raise ValueError("Некорректный возраст")
        self._age = new_age

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        try:
            self.name = new_name
        except ValueError as e:
            print(f"Ошибка: {e}")

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        try:
            self.age = new_age
        except ValueError as e:
            print(f"Ошибка: {e}")

# Создание нового пользователя
user = User('Иван', 30)

# Получение имени и возраста
print(user.get_name())  # Иван
print(user.get_age())   # 30

# Изменение имени
user.set_name('Петр')
print(user.get_name())  # Петр

# Ошибки при установке неправильных значений
try:
    user.set_name("123")       # Некорректное имя
    user.set_age(-10)          # Некорректный возраст
except ValueError as e:
    print(f"Ошибка: {e}")
