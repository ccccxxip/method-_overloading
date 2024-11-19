class Negator:
    @staticmethod
    def neg(value):
        if isinstance(value, (int, float)):
            return -value
        elif isinstance(value, bool):
            return not value
        else:
            raise TypeError("аргумент переданного типа не поддерживается")

''' пример использования '''

if __name__ == "__main__":
    print(Negator.neg(3.14))
    print(Negator.neg(-1))
    print(Negator.neg(0))

    try:
        print(Negator.neg("string"))
    except TypeError as e:
        print(e)
