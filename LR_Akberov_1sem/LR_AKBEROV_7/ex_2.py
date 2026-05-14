# Суперкласс содержит приватное текстовое поле.
# Есть метод set_value(text) для присваивания поля.
# Конструктор принимает один текстовый аргумент.
# Добавьте метод get_length(), возвращающий длину строки.
# Подкласс добавляет публичное целочисленное поле.
# В подклассе переопределите set_value() четырьмя вариантами:
# без параметров, с текстом, с числом, с текстом и числом.
# Конструктор подкласса принимает целое число и текст.


class SuperClass:

    def __init__(self, text : str):
        self.__text = text

    def set(self,text : str = None):
        if text is not None:
            self.__text = text

    def get_leanght(self):
        if self.__text != None:
            return f'Длинна строки - {len(self.__text)}'
        else:
            return f'Длинна строки - 0'

    def get_text(self):
        return self.__text

class SubClass(SuperClass):

    def __init__(self, number : int = None, text : str = None):
        if text != None:
            super().__init__(text)
        else:
            super().__init__('')
        self.number = number

    def set(self, number : int = None ,text : str = None):
        if number != None and text != None:
            super().set(text)
            self.number = number
        elif number != None and text == None:
            self.number = number
        elif number == None and text == None:
            super().set('')
        elif number == None and  text != None:
            super().set(text)

    def __str__(self):
        return f'Имя подкласса - {self.get_text()}, число "{self.number}", {self.get_leanght()} '

pt = SubClass(1,'world')
print(pt)

pt.set(number = 42)
print(pt)

pt.set(text='hello')
print(pt)

pt.set(text = 'a', number = 99)
print(pt)

pt.set()
print(pt)

