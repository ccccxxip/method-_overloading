from datetime import date, datetime

class BirthInfo:
    def __init__(self, birth_date):
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        elif isinstance(birth_date, str):
            try:
                self.birth_date = datetime.fromisoformat(birth_date).date()
            except ValueError:
                raise TypeError("аргумент переданного типа не поддерживается")
        elif isinstance(birth_date, (list, tuple)) and len(birth_date) == 3:
            year, month, day = birth_date
            try:
                self.birth_date = date(year, month, day)
            except ValueError:
                raise TypeError("аргумент переданного типа не поддерживается")
        else:
            raise TypeError("аргумент переданного типа не поддерживается")

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

# примкр использования
if __name__ == "__main__":
    birthinfo1 = BirthInfo(date(2023, 2, 26))
    print(birthinfo1.age)

    birthinfo2 = BirthInfo("2023-02-26")
    print(birthinfo2.age)

    birthinfo3 = BirthInfo([2023, 2, 26])
    print(birthinfo3.age)

    birthinfo4 = BirthInfo((2023, 2, 26))
    print(birthinfo4.age)

    # пример с некорректным типом
    try:
        birthinfo5 = BirthInfo("invalid date")
    except TypeError as e:
        print(e)
