# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

#n= int(input("Введите n: "))
#data = random.sample(range(-n, n+1), n+1)

data = [2, 3, 5, 9, 3]
sum = 0

# for idx, i in enumerate(data):
#    if idx % 2:
#        sum += i

for item in data[1::2]:
    sum += item

print(sum)
