# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

n = int(input("Введите n: "))
data = random.sample(range(-n, n), n)
#data = [2, 3, 4, 5, 6]
#data = [2, 3, 5, 6]
print("Исходный массив: ", data)
muldata = []

for i in range((len(data)+1)//2):
    muldata.append(data[i]*data[-i-1])

print(muldata)
