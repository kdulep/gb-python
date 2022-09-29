# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input("Введите n: "))
data = []
# если это рандомные [-N, N]
data = random.sample(range(-n, n+1), n*2+1)

# если это просто числа по порядку от -N до N
# for i in range(-n, n+1):
#     data.append(i)

print("Исходный список:", data)

file = open("file.txt", "r")
lines = [x.strip("\n") for x in file.readlines()]

print("Интересующие позиции из файла: ", lines)

mult = 1

for i in lines:
    mult *= data[int(i)]

print(mult)
