# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def Dec2Bin(num):
#     if num >= 1:
#         Dec2Bin(num // 2)
#     print(num % 2, end = '')

def tobin(x, s):
    return [(x >> k) & 1 for k in range(0, s)]


def trans(x):
    if x == 0:
        return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]


# Dec2Bin(45)
print(tobin(45, 8))
print(''.join(str(x) for x in trans(45)))
