import random


def play(n, m, players):
    turn = 0
    while n > 0:
        print("Ваш ход", f'{players[turn%2]} ')
        candys = int(input("Сколько конфет? "))
        while candys > n or candys > m:
            if n >= candys <= m:
                break
            candys = int(input("Неверно, Сколько конфет? "))
        n = n - candys
        if n > 0:
            print(f'Осталось {n} конфет')
        else:
            print('конфет больше нет')
        turn += 1
    return players[not turn % 2]


print("Игра 'забери все конфеты!'")

player1 = input('Первый игрок, как к Вам можно обращаться?\n')
player2 = input('Второй игрок, как к Вам можно обращаться?\n')
players = [player1, player2]

n = int(input('Сколько конфет всего?\n '))
m = int(input('Сколько максимально конфет за один ход?\n '))

playerwin = play(n, m, players)
if not playerwin:
    print('У нас нет победителя.')
else:
    print(f'Победил {playerwin}! Ему достаются все конфеты!')
