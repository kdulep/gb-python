
from tabulate import tabulate


message = '''Что делаем?
0-просмотр
1-добавить запись
2-удалить запись ученика под номером N
3-изменить запись ученика N
4-выход\n'''


def display_data(data):
    # for line in data:
    #     print(tabulate([line]))
    print(tabulate(data))


def display_menu():
    answer = int(input(message))
    return answer


def input_new_data(prompt):
    str_data = input(prompt)
    #update str_data = "1\tSid2\t01.01.2001\t7a\t2\t3"
    #add str_data = "Sid2\t01.01.2001\t7a\t2\t3"
    print(str_data)
    row = str_data.split("\t")
    #print(tabulate(row))
    return row
