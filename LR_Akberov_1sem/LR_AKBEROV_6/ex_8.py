# 8. Напишите программу со статическим методом, аргументом
# которому передается целочисленный массив, а результатом возвращается
# среднее значение для элементов массива (сумма значений элементов,
# деленная на количество элементов в массиве).

class Task7:

    def __init__(self):
        self.medium = 0
    def replace(self,val):
        self.medium = sum(val)/len(val)
        return print(self.medium)


pt = Task7()
try:
    pt.replace(list(map(int, input("Введите значения списка через пробел: ").split())))
except ValueError:
    print("Это не список")