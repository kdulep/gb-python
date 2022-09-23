# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def calcLength(a, b):
    return ((b[0]-a[0]) ** 2 + (b[1]-a[1]) ** 2)**(0.5)


def inputNumber(prompt):
    print(prompt)
    data = list(map(int, input().split()))
    return data

A = inputNumber("Enter the number 1 coordinates: X Y delimited by spaces")
B = inputNumber("Enter the number 2 coordinates: X Y delimited by spaces")

print("Line length:%.2f" %calcLength(A,B))
