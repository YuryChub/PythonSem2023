# 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# Пример: 
# 5 -> 1 0 1 1 0
# 2

import os
os.system('cls')
print('Введите количество монет')
vsegomonet = int(input())
orel = reshka = 0

for _ in range(vsegomonet):
    count = int(input('орел или решка (1 или 0) ? : '))
    if count == 1:
        orel += 1
    else:
        reshka += 1 
if orel > reshka:
    print(reshka)
else:
    print(orel)