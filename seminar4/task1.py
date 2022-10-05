# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

import decimal
from decimal import Decimal
import locale

precision_str = input("Precision: ")
precision = precision_str[::-1].find(locale.localeconv()["decimal_point"])
number = input("Number: ")
if precision > 0:
    decimal.getcontext().prec = precision+1

print(Decimal(number)+Decimal(0))
