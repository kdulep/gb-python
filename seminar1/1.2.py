# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
        print('I четверть')
    if xcoord > 0 and ycoord < 0:
        print('IV четверть')
    if xcoord < 0 and ycoord > 0:
        print('II четверть')
    if xcoord < 0 and ycoord < 0:
        print('III четверть')


print("Enter the numbers: X Y delimited by spaces")
data = list(map(int, input().split()))

x = data[0]
y = data[1]

quarter(x, y)
