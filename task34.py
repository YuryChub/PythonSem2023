# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

import os
os.system('cls')
dict = {"аеёиоуыэюя": 1}
phrase = input('введите песенку: ').split()
sum = 0
sum_out = []

for word in phrase:
    for j in word:
        for i in dict.items():
            if j.lower() in i[0]:
                sum = sum + (i[1])
    sum_out.append(sum)
    sum = 0
if sum_out.count(sum_out[0]) == len(sum_out) and sum_out[0] != 0:
    print("Парам пам-пам")
else:
    print("Пам парам")
