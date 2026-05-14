# 5. Напишите программу со статическим методом, которым вычисляется
# сумма квадратов натуральных чисел 1**2 + 2**2 + 3**2 + ... + п2.
# Число п передается аргументом методу. Для проверки результата
# можно использовать формулу 12 + 22 +32+…+n2=(n+l) (2n + 1)/6

class Task5:
    def sum_of_squares(self,val):
        val_sofs = 0
        for i in range(1,val+1):
            val_sofs +=i**2
        check = (val * (val + 1)*(2 * val + 1))/6
        print(check)
        if check == val_sofs:
            print('Код работает верно')
        else:
            print('Код работает некорректно')
        return print(val_sofs)

pt = Task5()
try:
    pt.sum_of_squares(int(input('Введите число: ')))
except ValueError:
    print('Введите целое число')


