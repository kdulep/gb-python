# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11

import locale

def summa(num):
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    return sum

num = input("Введите вещественное число: ")
sum = 0
if locale.localeconv()["decimal_point"] in num:
    x = num.split(locale.localeconv()["decimal_point"])
    a = int(x[0])  # целая часть
    b = int(x[1])  # дробная часть
    sum = summa(a)+summa(b)
else:
    a = int(num)
    sum = summa(a)

print("Сумма цифр числа равна: ", sum)
