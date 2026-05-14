# 3. Напишите программу с классом, в котором есть статические
# методы, которым можно передавать произвольное количество целочисленных
# аргументов (или целочисленный массив). Методы, на основании переданных
# аргументов или массива, позволяют вычислить: наибольшее значение,
# наименьшее значение, а также среднее значение из набора чисел.

class Task3:

    def __init__(self):
        self.data = []
    def statick(self,*args):
        data = []
        list(args)
        args = args[0]
        print(type(args))
        if type(args) == list:
            for i in range(len(args)):
                if isinstance(args[i],int):
                    self.data.append(args[i])
        elif type(args) == int:
            if  isinstance(args,int):
                self.data.append(args)
        else:
            raise ValueError('Вы не ввели значение(я)')
        return print(self.data)

pt = Task3()
k = 0
while k != 1:
    type_value = input('тип данных для ввод? int или list(i/l): ').lower()
    if type_value == 'l':
        try:
            val_list = (list(map(int, input('введите список из чисел через пробел').split())))
            pt.statick(val_list)
        except ValueError:
            print('В списке должны быть только целые числа')
            continue
    elif type_value == 'i':
        try:
            val_int = int(input('введите число'))
            pt.statick(val_int)
        except ValueError:
            print('Значение должно быть единственным числом')
            continue
    else:
        raise ValueError('Вы ввели некорректное значение')
    answer = input('Продолжить ввод данных? (y/n): ').lower()
    if answer == 'y' or answer == 'n':
        if answer == 'n':
            k +=1
    else:
        raise ValueError('Вы вели некоректное значение')
print(f'максимальное значение: {max(pt.data)}, минимальное значение: {min(pt.data)}, среднее значение: {sum(pt.data)/len(pt.data)}')
