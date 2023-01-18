# Создайте программу для игры в ""Крестики-нолики"".

import random

def print_map(game_board):
    print('Игровое поле и нумерация ячеек выглядят следующим образом:')
    print(f'1:{game_board[0]}\t 2:{game_board[1]}\t 3:{game_board[2]}\t')
    print(f'4:{game_board[3]}\t 5:{game_board[4]}\t 6:{game_board[5]}\t')
    print(f'7:{game_board[6]}\t 8:{game_board[7]}\t 9:{game_board[8]}\t')
    print()
    print('Игрок под номером 1 играет Х')
    print('Игрок под номером 2 играет 0')
    print()

def check_win(game_board):
    winner = ''
    if  (game_board[0] != '') and (game_board[0] == game_board[1] == game_board[2]): winner = game_board[0]
    if  (game_board[3] != '') and (game_board[3] == game_board[4] == game_board[5]): winner = game_board[3]
    if  (game_board[6] != '') and (game_board[6] == game_board[7] == game_board[8]): winner = game_board[6]
    if  (game_board[0] != '') and (game_board[0] == game_board[3] == game_board[6]): winner = game_board[0]
    if  (game_board[1] != '') and (game_board[1] == game_board[4] == game_board[7]): winner = game_board[1]
    if  (game_board[2] != '') and (game_board[2] == game_board[5] == game_board[8]): winner = game_board[2]
    if  (game_board[0] != '') and (game_board[0] == game_board[4] == game_board[8]): winner = game_board[0]
    if  (game_board[1] != '') and (game_board[2] == game_board[4] == game_board[6]): winner = game_board[2]
    if winner == 'X':
        print_map(game_board)
        print(f'Игра закончилась. Поздравляем игрока под номером 1 с победой!')
        return True;
    elif winner == '0':
        print_map(game_board)
        print(f'Игра закончилась. Поздравляем игрока под номером 2 с победой!')
        return True;
    else:
        return False

print('Игра "Крестики-Нолики"')
active_player = random.randint(1, 2)
signs_player = {1: 'X', 2: '0'}

game_active = True;
game_board = ['', '', '', '', '', '', '', '', '']

while game_active:
    if active_player == 1: active_player = 2
    else: active_player = 1
    print_map(game_board)
    game_turn = int(input(f'Игрок под номером {active_player} сделайте ход (укажите номер ячейки от 1 до 9): '))  
    if game_turn > 0 and game_turn < 10:
        if game_board[game_turn-1]  == '':
            game_board[game_turn-1] = signs_player[active_player]
            if check_win(game_board):
                game_active = False;
            elif '' not in game_board:
                print(f'На поле закончились ячейки. Игра закончилась ничьей. Победила дружба!')
                game_active = False;
        else:
            print('Ячейка занята. Начнем ход заново.')
    else:
        print(f'Игрок под номером {active_player} жульничает. Начнем ход заново.')