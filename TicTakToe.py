# Создайте программу для игры в ""Крестики-нолики".

import os


def clear(): return os.system('cls')


def draw_field():
    clear()
    print()
    for i in range(0, 9, 3):
        print('-' * 13 + ' ' * 8 + '-' * 13)
        print(
            f"| {cells[i]} | {cells[i+1]} | {cells[i+2]} |        | {i+1} | {i+2} | {i+3} |")
    print('-' * 13 + ' ' * 8 + '-' * 13 + '\n')


def check_win(gamer):

    def f(a): return a == gamer

    return any([all(map(f, cells[:3])),
                all(map(f, cells[3:6])),
                all(map(f, cells[6:])),
                all(map(f, cells[::3])),
                all(map(f, cells[1::3])),
                all(map(f, cells[2::3])),
               all(map(f, (cells[0], cells[4], cells[8]))),
               all(map(f, (cells[2], cells[4], cells[6])))
                ])


cells = [' '] * 9
gamer = 'X'
is_win = False
step = 0

while True:
    draw_field()
    print(f"Игрок  {gamer}:")
    print("введите номер поля (подсказка справа)")
    move = False

    while not move:
        move = input()
        if move.isdigit() and 0 < int(move) < 10:
            move = int(move)
        else:
            print("Пожалуйста, вводите только числа от 1 до 9!")
            move = False
            continue

        if cells[move - 1] == ' ':
            cells[move - 1] = gamer
        else:
            print("Это поле уже занято, введите другое")
            move = False
            continue

    step += 1
    if step > 4:
        is_win = check_win(gamer)

    if is_win:
        draw_field()
        print(f"{gamer} победил!\n")
        input('>>')
        break

    if step == 9:
        draw_field()
        print("Ничья!\n")
        input('>>')
        break

    gamer = 'O' if gamer == 'X' else 'X'
