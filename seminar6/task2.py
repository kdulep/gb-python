# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

import random
from collections import Counter
n = int(input("Введите n: "))
data = []

for i in range(n):
    n = random.randint(1, 10)
    data.append(n)

print("Исходные данные", data)

data_dedup = set(data)

uniq_list = []
dup_list = []
data_count = dict(Counter(data))
# print(data_count)
for d in data_dedup:
    if data_count[d] == 1:
        uniq_list.append(d)
    else:
        dup_list.append(d)

print("Уникальные: ", uniq_list)
print("Повторяемые: ", dup_list)
print("Без дубликатов: ", data_dedup)
