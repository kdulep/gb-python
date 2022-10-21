import fileio
import display

data = []


def main_loop():
    while True:
        answer = display.display_menu()
        if answer == 0:
            data = fileio.read_data()
            display.display_data(data)
        elif answer == 1:
            row = display.input_new_data(
                '''Please enter new data delimited by tabs:fio, birthdate, name, rowname,colname:\n''')
            fileio.write_data((row[0], row[1], row[2], row[3], row[4]))
            data = fileio.read_data()
            display.display_data(data)
        elif answer == 2:
            str_to_del = input("Please enter ID: ")
            fileio.delete_data(str_to_del)
            data = fileio.read_data()
        elif answer == 3:
            row = display.input_new_data(
                '''Please enter updated data delimited by tabs:id, fio, birthdate, name, rowname,colname:\n''')
            fileio.update_data(
                (row[0], row[1], row[2], row[3], row[4], row[5]))
        elif answer == 4:
            return
        else:
            print("Повторите выбор")
