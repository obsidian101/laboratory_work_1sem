# Создайте три класса в цепочке наследования.
# Первый класс имеет публичное целочисленное поле.
# Метод set(value) и конструктор с одним параметром.
# Второй класс добавляет публичное символьное поле.
# Метод set(value, symbol) перегружает родительский метод.
# Конструктор с двумя параметрами.
# Третий класс добавляет публичное текстовое поле.
# Метод set(value, symbol, text) — перегрузка.
# Конструктор с тремя параметрами.
# В каждом классе переопределите str для отображения
# названия класса и всех его полей.

class SuperClass:
    def __init__(self, value: int):
        self.number = value

    def set(self, value: int):
        self.number = value

    def __str__(self):
        return f"FirstClass: value = {self.number}"


class SecondClass(SuperClass):
    def __init__(self, value: int, symbol: str):
        super().__init__(value)
        self.symbol = symbol

    def set(self, value: int, symbol: str = None):
        super().set(value)
        if symbol is not None:
            self.symbol = symbol

    def __str__(self):
        return f"SecondClass: value = {self.number}, symbol = '{self.symbol}'"


class ThirdClass(SecondClass):
    def __init__(self, value: int, symbol: str, text: str):
        super().__init__(value, symbol)
        self.text = text

    def set(self, value: int = None, symbol: str = None, text: str = None):
        if value is not None:
            super().set(value, symbol)
        elif symbol is not None:
            self.symbol = symbol
        if text is not None:
            self.text = text

    def __str__(self):
        return f"ThirdClass: value = {self.number}, symbol = '{self.symbol}', text = '{self.text}'"


# Проверка
pt = SuperClass(1)
pt1 = SecondClass(2, "A")
pt2 = ThirdClass(3, "B", "Hello")

print(pt)
print(pt1)
print(pt2)
print()

pt2.set(100)
print(pt2)
pt2.set(200, 'C')
print(pt2)
pt2.set(300, 'D', "World")
print(pt2)