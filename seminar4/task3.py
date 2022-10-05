# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
import random

n = int(input("Введите n: "))
#data = [1, 3, 5, 5, 1]
#data = random.sample(range(n), n*2+1)
data=[]
for i in range(n):
    n = random.randint(1,10)
    data.append(n)

print(data)
unique_numbers = list(set(data))
print(unique_numbers)
