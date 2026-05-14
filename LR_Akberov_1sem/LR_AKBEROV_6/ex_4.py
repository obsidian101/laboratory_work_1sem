# 4. Напишите программу, в которой описан статический метод для вычисления
# двойного факториала числа, переданного аргументом методу.
# По определению, двойной факториал числа п (обозначается как n!!)
# — это произведение через одно всех чисел, не больших числа п.
# То есть n!! = п * (n - 2) * (п - 4)* ... (последний множитель равен 1
# для нечетного п и равен 2 для четного n).
# Например, 6!! = 6 х 4 х 2 = 48 и 5!! = 5 х 3 х 1 = 15.

class Task4:

    def __init__(self):
        self.lst = []
        self.val_fac = 0
    def doubl_factorial(self,val):
        self.val_fac +=val
        if val % 2 == 0:
            for i in range(2,val,2):
                self.lst.append(i)
            for j in range(len(self.lst)):
                self.val_fac *=(self.lst[j])
            return print(self.val_fac)
        elif val % 2 == 1:
            for i in range(1, val, 2):
                self.lst.append(i)
            for j in range(len(self.lst)):
                self.val_fac *= (self.lst[j])
            return print(self.val_fac)

pt = Task4()
try:
    a = int(input('Введите целое число: '))
    pt.doubl_factorial(a)
except ValueError:
    print('Введите корректное значение')


