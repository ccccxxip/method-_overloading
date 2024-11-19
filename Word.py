class Word:
    def __init__(self, word):
        if not word.isalpha():
            raise ValueError("Слово должно содержать только латинские буквы")
        self.word = word

    def __repr__(self):
        return f'Word({self.word!r})'

    def __str__(self):
        return self.word.capitalize()

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Word):
            return len(self.word) > len(other.word)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Word):
            return len(self.word) <= len(other.word)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Word):
            return len(self.word) >= len(other.word)
        return NotImplemented

# Создаем несколько экземпляров класса Word
w1 = Word("hello")
w2 = Word("world")
w3 = Word("python")

# Формальная строковая репрезентация
print(repr(w1))     # Word('hello')
print(repr(w2))     # Word('world')
print(repr(w3))     # Word('python')

# Неформальная строковая репрезентация
print(str(w1))      # Hello
print(str(w2))      # World
print(str(w3))      # Python

# Сравнения
print(w1 == w2)     # False
print(w1 != w2)     # True
print(w1 > w2)      # False
print(w1 < w2)      # True
print(w1 >= w3)     # False
print(w1 <= w3)     # False
