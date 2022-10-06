# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal

precision_str = Decimal(input("Precision: "))
number = Decimal(input("Number:"))

print(number.quantize(precision_str))
