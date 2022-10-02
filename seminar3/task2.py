# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

n= int(input("Введите n: "))
data = random.sample(range(-n, n), n)
print ("Исходный массив: ",data)
#data = [2, 3, 4, 5, 6]
#data = [2, 3, 5, 6]
muldata = []

#datalen=len(data) #можно но не нужно ухудшать читаемость кода из за O(1) функции
# https://stackoverflow.com/questions/1115313/cost-of-len-function
#it's O(1) (constant time, not depending of actual length of the element - very fast)

for i in range(0, int(len(data)/2)):
    muldata.append(data[i]*data[-i-1])

if not len(data) % 2 == 0:
    muldata.append(data[int(len(data)/2)]**2)

print(muldata)
