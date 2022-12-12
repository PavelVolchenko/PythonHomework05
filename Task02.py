""" Создайте программу для игры с конфетами человек против человека.
    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
    ход друг после друга. Первый ход определяется жеребьёвкой. За один ход
    можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
    сделавшему последний ход. Сколько конфет нужно взять первому игроку,
    чтобы забрать все конфеты у своего конкурента?
    a) Добавьте игру против бота
    b) Подумайте как наделить бота ""интеллектом""                     """

import random


def turn(who, candy):
    if candy > 28:
        max_candies = 28
    else:
        max_candies = candy
    if who == 0:
        return 1, player_action(player_one, max_candies, candy)
    else:
        if candy <= 28:
            print(f'\nКОМПЬЮТЕР - забирает все конфеты со стола. Их оставалось {candy}.')
            return 0, candy - candy
        elif candy < 112:
            for i in range(1, 29):
                if (candy - i) == 57 or (candy - i) == 84:
                    print(f'КОМПЬЮТЕР - берет {i} конфет. На столе осталось {candy - i} конфет.')
                    return 0, candy - i
        for i in range(1, 29):
            if (candy - i) % 28 == 1:
                print(f'КОМПЬЮТЕР - берет {i} конфет. На столе осталось {candy - i} конфет.')
                return 0, candy - i


def player_action(player, max_candies, candy):
    while True:
        print(f'Конфет на столе: {candy}')
        print(f"{player['name']} - твой ход. Сколько конфет возьмешь? ", end=' ')
        count_candies = int(input())
        if 1 <= count_candies <= max_candies:
            candy -= count_candies
            return candy
        else:
            print(f"Ты должен взять минимум 1 конфету, но не больше {max_candies} конфет!")


# candies = 2021
candies = 256
player_one = {'name': 'ЧЕЛОВЕК'}
player_two = {'name': 'КОМПЬЮТЕР'}
flag = random.randint(0, 1)
print('\t\t*** Игра про конфеты ***\n ')
if flag == 0:
    print(f'Первым ходит {player_one["name"]}. Удачи!')
else:
    print(f'Первым ходит {player_two["name"]}. Он кстати, никогда не проигрывает!')
while candies > 0:
    flag, candies = turn(flag, candies)
if flag == 1:
    print(f'\t\n***** {player_one["name"]} ВЫИГРАЛ! КАК У ТЕБЯ ПОЛУЧИСЛОСЬ? *****')
else:
    print(f'\n\t***** {player_two["name"]} СНОВА ПОБЕДИЛ! *****')
