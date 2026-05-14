# 5. Напишите программу, в которой создается двумерный целочисленный массив. Он заполняется случайными числами.
# Затем в этом массиве строки и столбцы меняются местами: первая строка становится первым столбцом, вторая строка
# становиться вторым столбцом и так далее. Например, если исходный массив состоял из 3 строк и 5 столбцов, то в итоге
# получаем массив из 5 строк и 3 столбцов.

import random
he, wi = int(input()), int(input())
matrix = []

for i in range(he):
    row = []
    for j in range(wi):
        row.append(random.randint(0,9))
    matrix.append(row)

for i in range(he):
    for j in range(wi):
        print(matrix[i][j], end=' ')
    print()
print('')

for i in range(wi):
    for j in range(he):
        print(matrix[j][i], end=' ')
    print()
