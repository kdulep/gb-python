# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
import random
from collections import Counter

n = int(input("Введите n: "))
#data = [1, 3, 5, 5, 1]
#data = random.sample(range(n), n*2+1)
data = []
for i in range(n):
    n = random.randint(1, 10)
    data.append(n)

print(data)

newlist = []
data_count = dict(Counter(data))

for d in data:
    if data_count[d] == 1:
        newlist.append(d)

print(newlist)
