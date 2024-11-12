import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle(self):
        return math.degrees(math.atan2(self.y, self.x))

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Пример использования
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("Длина вектора v1:", v1.length())
print("Угол наклона вектора v1:", v1.angle())
print("Сумма векторов v1 и v2:", v1.add(v2))
print("Разность векторов v1 и v2:", v1.subtract(v2))
print("Скалярное произведение векторов v1 и v2:", v1.dot_product(v2))