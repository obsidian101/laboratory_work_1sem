# 2. Напишите программу, которая выводит в консольное окно прямоугольный треугольник;

size = int(input())
he , wi = size, size
k = 0
for i in range(he):
    for j in range(wi):
        if j == 0 or i == he -1 or j == k:
            print('*', end='')
        else:
            print(' ', end='')
    k += 1
    print()


