# 6. Напишите программу, в которой создается и инициализируется двумерный числовой массив. Затем из этого массива
# удаляется строка и столбец (создается новый массив, в котором по сравнению с исходным удалена одна строка и один
# столбец). Индекс удаляемой строки и индекс удаляемого столбца определяется с помощью генератора случайных чисел.

import random
matrix = []

he = random.randint(3,6)
wi = random.randint(3,6)


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

coppy_matrix = matrix.copy()
del_rand_wi = random.randint(0,wi)

del coppy_matrix[random.randint(0,he - 1)]

for i in range(he-1):
    for j in range(wi):
        if j == del_rand_wi:
            del coppy_matrix[i][j]

for i in range(he-1):
    for j in range(wi-1):
        print(matrix[i][j], end=' ')
    print()








