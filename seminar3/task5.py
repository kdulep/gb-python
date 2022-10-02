# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части
# элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

#n= int(input("Введите n: "))
#data = [round(random.uniform(0,n),2) for _ in range(n)]
data = [1.1, 1.2, 3.1, 5, 10.01]

print("Исходный массив: ", data)
min = data[0]-int(data[0])
max = min
for value in data[1:]:
    intpart, decimalpart = int(value), value-int(value)

    if decimalpart == 0:
        continue

    if decimalpart > max:
        max = decimalpart

    if decimalpart < min:
        min = decimalpart

print("decimal fraction max-min: ", round(max-min, 2))
