# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("Input week day number:"))

if 1 <= a <= 5:
    print("Not weekend")

elif a == 6 or a == 7:
    print("Weekend")

else:
    print("Wrong weekday number")
