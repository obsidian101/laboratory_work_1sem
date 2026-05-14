# 4. Напишите программу, в которой создается двумерный массив, который выводит прямоугольный треугольник;
size = int(input())
he, wi = size, size
matrix = []
for i in range(he):
    row = []
    for j in range(wi):
        row.append("*")
        matrix.append(row)
for i in range(he):
    for j in range(wi):
        if i >= j:
            print(matrix[i][j], end=' ')
    print()
