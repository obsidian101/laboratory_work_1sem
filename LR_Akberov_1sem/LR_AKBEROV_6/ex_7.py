# 7. Напишите программу со статическим методом, аргументом
# которому передастся символьный массив, а результатом возвращается ссылка
# на целочисленным массив, состоящий из кодов символов из массива- аргумента.
class Task7:

    def __init__(self):
        self.rpl = []
    def replace(self,val):
        for i in val:
            self.rpl.append(ord(i))
        return print(self.rpl)

pt = Task7()
pt.replace(input())
