# Напишите класс с приватным строковым полем
# длины один. Добавьте три публичных метода.
# Первый метод присваивает значение этому полю.
# Второй метод возвращает числовой код символа.
# Третий метод печатает сам символ и его код.

import random
class Str:
    __str = " "

    @classmethod
    def fun_1(cls, arg):
        if len(arg) == len(cls.__str):
            cls.__str = arg
            print(Str.__dict__)
        else:
            cls.__str = chr(random.randint(65, 122))
            print(f'Т.К длинна строки не была равной 1 мы ввели случайное значение - {cls.__str}')

    def fun_2(self):
        return self.__str

    def fun_2(self):
        return self.__str, ord(self.__str)

pt = Str()
Str.fun_1("hi")
print(pt.fun_2())

