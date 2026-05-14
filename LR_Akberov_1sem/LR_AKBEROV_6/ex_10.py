class Task10:

    def __init__(self):
        self.lst = []

    def max_min(self,val):
        self.lst.append(min(val))
        self.lst.append(max(val))
        return self.lst , print(self.lst )

pt = Task10()
try:
    pt.max_min(list(map(int, input("Введите значения списка через пробел: ").split())))
except ValueError:
    print('Введите список состящий из целых чисел')

