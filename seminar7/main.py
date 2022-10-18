# Написать программу по импорту и экспорту телефонного справочника состоящий из N тысяч строк, содержащих информацию о неких пользователях.
# Предлагаемые поля: id, имя, фамилия, день рождения, место работы, номер телефона (может быть несколько). В качестве символа разделителя использовать пустую строку (пустой символ).
# Программа должна быть модульной (как показывалось на уроке). Она должна уметь генерировать справочник и сохранять его в файл при необходимости (экспорт) или загружать (импорт). Также необходимо организовать просмотр информации из справочника (генерируемого или загружаемого).
# В качестве формата файла можно использовать форматы csv, json, xml

import fileio
import display

data = fileio.read_data("data.csv")
display.display_data(data)

while True:
    answer = display.display_menu()
    if answer == 0:
        display.display_data(data)
    elif answer == 1:
        str_data = input("Please enter your data delimited by tabs: ")
        row = str_data.split("\t")
        data.append([row[0], row[1], row[2], row[3], row[4]])
    elif answer == 2:
        str_to_del = input("Please enter ID: ")
        for i in range(len(data)):
            if data[i][0] == str_to_del:
                del (data[i])
    elif answer == 3:
        fileio.write_data("data.csv", data)
    elif answer == 4:
        exit()
    else:
        print("Повторите выбор")
