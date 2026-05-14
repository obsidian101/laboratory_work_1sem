# Создайте суперкласс с приватным текстовым полем.
# Конструктор принимает текстовый параметр.
# Переопределите метод str для вывода названия класса
# и значения поля.
# Создайте подкласс с дополнительным приватным текстовым полем.
# В подклассе реализуйте два конструктора: с одним
# и с двумя текстовыми аргументами.
# Переопределите str для вывода обоих полей


class Superclass:

    def __init__(self, text:str):
        self.__text1 = text

    def __str__(self):
        class_name = self.__class__.__name__
        return f'Имя класса - {class_name}, поле класса - "{self.__text1}"'
    def get_text(self):
        return self.__text1

class SubClass(Superclass):

    def __init__(self, text1 : str,text2 : str = None):
        super().__init__(text1)
        if text2 == None:
            self.__text2 = ' '
        else:
            self.__text2 = text2

    def __str__(self):
        class_name = self.__class__.__name__
        return f'Имя класса - "{class_name}", поле text1 - "{self.get_text()}", поле text2 - "{self.__text2}"'

pt = SubClass('hello','world')
print(pt)

pt1 = SubClass('hi')
print(pt1)

pt2 = Superclass('hi')
print(pt2)