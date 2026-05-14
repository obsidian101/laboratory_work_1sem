# Постройте цепочку из трёх классов.
# Первый класс имеет публичное символьное поле.
# Второй класс добавляет публичное текстовое поле.
# Третий класс добавляет публичное целочисленное поле.
# В каждом классе реализуйте конструктор для инициализации
# полей переданными аргументами.
# Также в каждом классе создайте конструктор копирования.
import copy

class SuperClass:
    def __init__(self, symbol : str):
        self.symbol = symbol

    def set(self,symbol : str):
        self.symbol = symbol

    def __copy__(self):
        return SuperClass(self.symbol)

class SubClass(SuperClass):

    def __init__(self, symbol : str = None, txt : str = None):
        if symbol is not None:
            super().__init__(symbol)
        else:
            super().__init__('')
        self.txt = txt

    def set(self, symbol : str = None, txt : str = None):
        if symbol is not None:
            super().set(symbol)
        if txt is not None:
            self.txt = txt

    def __copy__(self):
        return SubClass(self.symbol, self.txt)

class ThirdClass(SubClass):

    def __init__(self, symbol : str = None, txt : str = None, val : int = None):
        if symbol is not  None:
            super().__init__(symbol)
        else:
            super().__init__('')
        if txt is not None:
            super().__init__(txt)
        else:
            super().__init__('')
        self.val = val

    def set(self, symbol : str = None, txt : str = None, val : int = None):
        if symbol is not None:
            super().set(symbol)
        if txt is not None:
            super().set(txt)
        if val is not None:
            self.val = val

    def __copy__(self):
        return ThirdClass(self.symbol, self.txt, self.val)


obj1 = ThirdClass("A", "Hello")
obj2 = obj1.__copy__()

print(f"obj1: symbol={obj1.symbol}, txt={obj1.txt}, val={obj1.val}")
print(f"obj2: symbol={obj2.symbol}, txt={obj2.txt}, val={obj2.val}")
print()

obj2.set(symbol="B", val=23)
print(f"После изменения obj2:")
print(f"obj1: symbol={obj1.symbol}, txt={obj1.txt}, val={obj1.val}")
print(f"obj2: symbol={obj2.symbol}, txt={obj2.txt}, val={obj2.val}")

