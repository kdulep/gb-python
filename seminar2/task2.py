# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def factorial(n):
#     product = 1
#     while n > 0:
#         product *= n
#         n -= 1
#     return product

#  def factorial(n):
#      if n <= 1: return 1
#      return n * factorial(n-1)

import math

N = int(input("Введите целое число:N "))
for i in range(1, N+1):
    print(math.factorial(i), end=' ')
