# 1. Напишите программу, которая выводить в консольное окно прямоугольник, размеры сторон которого, ширина:
# 23 колонки, высота: 11 строк;
he = int(input())
wi = int(input())
for i in range(he):
    for j in range(wi):
        if i == 0 or j == 0 or i == he -1 or j == wi -1:
            print('*', end='')
        else:
            print(' ', end='')
    print()