# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("Enter the numbers: XYZ delimited by spaces")
data = list(map(int, input().split()))

x = data[0]
y = data[1]
z = data[2]

print("x={0} y={1} z={2}".format(x, y, z))

if not (x or y or z) == (not x and not y and not z):
    print("Predicate True")
else:
    print("Predicate False")
