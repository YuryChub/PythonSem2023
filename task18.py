# 2 Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

import os
os.system('cls')
n = int(input('Введите количество элементов списка: '))
x = int(input('Введите число Х: '))
min_delta = float('inf')
delta = 0
A = []

for i in range(n):
    n = int(input('введите элемент списка : '))
    A.append(n)
    delta = abs(x - A[i])
    if delta < min_delta:
        min_delta = delta
        k = A[i]
print('Самый близкий к Х =', x , 'элемент списка =',k)
