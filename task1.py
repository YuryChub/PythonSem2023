# Найдите сумму цифр трехзначного числа.
# in 123 out 6
# in 100 out 1  

print('Введите любое натуральное число')
a = int(input())
i = 0
while a != 0:
    s = a % 10
    a = a//10
    i = i + s
print('Сумма цифр этого числа =', i)
