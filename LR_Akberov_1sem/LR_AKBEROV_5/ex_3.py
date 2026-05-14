# Напишите программу с классом, у которого есть два
# целочисленных поля. В классе должны быть описаны
# конструкторы, позволяющие создавать объекты без передачи
# аргументов, с передачей одного аргумента и с передачей двух
# аргументов.

class Task3:
    a = 0
    b = 0

    @classmethod
    def fun_1(cls,*args):
        if len(args) == 0:
            cls.a, cls.b = 0, 0
            print(cls.a, cls.b)
        if len(args) ==1:
            cls.a = args[0]
            print(cls.a, cls.b)
        if len(args) == 2:
            cls.a, cls.b = args[0], args[1]
            print(cls.a, cls.b)
        else:
            return ('Кол аргументов может быть 0,1,2')

Task3.fun_1(1)
