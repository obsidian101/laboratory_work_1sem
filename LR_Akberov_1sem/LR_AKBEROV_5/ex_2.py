# Напишите класс с двумя строковыми полями.
# Создайте метод без аргументов, возвращающий результат.
# Он выводит в консоль все символы кодовой
# таблицы между значениями этих двух полей.
# Например, если поля равны 'A' и 'D',
# будут напечатаны 'A', 'B', 'C', 'D'.
#

# *
# Я так пониамю задача нерешаема, с условием -
# 'Создайте метод без аргументов'
# *

lis = []
class Task1:
    val_1 = ''
    val_2 = ''

    @classmethod
    def fun_1(cls,arg_1, arg_2):
        cls.val_1 = arg_1
        cls.val_2 = arg_2
        if ord(cls.val_1) > ord(cls.val_2):
            cls.val_1 , cls.val_2 = cls.val_2 , cls.val_1
            for i in range(ord(cls.val_1),ord(cls.val_2)+1):
                lis.append(chr(i))
            print(lis)
        else:
            for i in range(ord(cls.val_1),ord(cls.val_2)+1):
                lis.append(chr(i))
            print(lis)

print(Task1.fun_1(input(),input()))





