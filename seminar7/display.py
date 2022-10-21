message = '''Что делаем?
0-просмотр
1-добавить запись
2-удалить запись под номером N
3-записать в файл
4-выход\n'''


def display_data(data):
    for line in data:
        print(line)


def display_menu():
    answer = int(input(message))
    return answer
