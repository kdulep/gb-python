# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

def fn(n):
    return (1+1/n)**n

data = []
sum=0

n = int(input("Введите n: "))

for i in range(1, n+1):
    data.append(fn(i))
    sum=sum+data[-1]

print(sum)