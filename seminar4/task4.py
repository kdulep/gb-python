# Задана натуральная степень k. Сформировать
# случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import numpy as np
from random import randint
from sympy import Symbol, expand

k = randint(2, 5)


def get_ratios(k):
    ratios = [randint(0, 100) for i in range(k + 1)]
    return ratios


#ratios = get_ratios(k)
ratios=[4,12,0]
print(ratios)
p = np.poly1d(ratios)
print(p)
x = Symbol('x')

with open('Polynomial.txt', 'w') as data:
    data.write(str(expand(p(x))).replace('**', '^')+" = 0")
