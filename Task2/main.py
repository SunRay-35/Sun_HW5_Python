# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. За один ход можно брать не больше 28 конфет. Побеждает тот, кто сделает последний ход.')

game_with_bot = bool(input('Хотите ли вы сыграть с ботом (0 - нет, 1 - да)? '))

if game_with_bot:
    print('Игра с ботом активирована, он играет по номером 2')
active_player = random.randint(1, 2)

print()

sweets_on_table = 2021
change = False

while sweets_on_table > 0:
    if change:
        if active_player == 1: active_player = 2
        else: active_player = 1
    change = True
    print(f'На столе {sweets_on_table} конфет. Ходит игрок под номером  {active_player}')
    if sweets_on_table > 28:
        sweets_max = 28
    else:
        sweets_max = sweets_on_table
    if game_with_bot and active_player == 2:
        if sweets_on_table - sweets_max >= 29: sweets_count = sweets_max
        elif sweets_on_table <= 28: sweets_count = sweets_on_table
        else: sweets_count = sweets_on_table - 29
        if sweets_count == 0: sweets_count = 1
        print(f'Бот выбирает число конфет {sweets_count}')
    else:
        sweets_count = int(input(f'Сколько конфет забирает со стола игрок под номером {active_player} (можно забрать от 1 до {sweets_max}): '))
    if sweets_count > 0 and sweets_count <= sweets_max:
        sweets_on_table -= sweets_count
    else:
        print(f'Игрок под номером {active_player} жульничает. Начнем ход заново.')
        change = False
        
print(f'Конфеты закончились. Последний ход сделал игрок под номером {active_player}. Поздравляем его с победой!')