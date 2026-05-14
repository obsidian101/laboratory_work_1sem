# 9. Напишите программу со статическим методом, аргументом
# которому передается одномерный символьный массив.
# В результате вызова метода элементы массива попарно меняются местами:
# первый — с последним, второй — с предпоследним и так далее.

class Task9:
    def __init__(self):
        self.lst = []
    def replace(self,val):
        val = ' ' + val
        for i in range(1,len(val)):
            print(i)
            self.lst.append(val[-1*i])
        return print(self.lst)

pt = Task9()
pt.replace('abcdf')
