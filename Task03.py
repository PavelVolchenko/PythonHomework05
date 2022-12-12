""" Создайте программу для игры в ""Крестики-нолики"". """


def winner():
    if field[0] == 'X' and field[1] == 'X' and field[2] == 'X' or\
            field[3] == 'X' and field[4] == 'X' and field[5] == 'X' or \
            field[6] == 'X' and field[7] == 'X' and field[8] == 'X' or \
            field[0] == 'X' and field[4] == 'X' and field[8] == 'X' or \
            field[2] == 'X' and field[4] == 'X' and field[6] == 'X' or \
            field[0] == 'X' and field[3] == 'X' and field[6] == 'X' or \
            field[2] == 'X' and field[5] == 'X' and field[8] == 'X' or \
            field[1] == 'X' and field[4] == 'X' and field[7] == 'X':
        print("ПОБЕДИЛИ - X\nИГРА ЗАКОНЧЕНА")
        return 1
    elif field[0] == 'O' and field[1] == 'O' and field[2] == 'O' or\
            field[3] == 'O' and field[4] == 'O' and field[5] == 'O' or \
            field[6] == 'O' and field[7] == 'O' and field[8] == 'O' or \
            field[0] == 'O' and field[4] == 'O' and field[8] == 'O' or \
            field[2] == 'O' and field[4] == 'O' and field[6] == 'O' or \
            field[0] == 'O' and field[3] == 'O' and field[6] == 'O' or \
            field[2] == 'O' and field[5] == 'O' and field[8] == 'O' or \
            field[1] == 'O' and field[4] == 'O' and field[7] == 'O':
        print("ПОБЕДИЛИ - O\nИГРА ЗАКОНЧЕНА!")
        return 1
    else:
        return 0


def turn(char, position):
    if field[position] == 'X':
        print("Эта клетка занята")
        return 0, 'X'
    elif field[position] == 'O':
        print("Эта клетка занята")
        return 0, 'O'
    field[position] = char
    for i in range(1, 10):
        if i % 3 == 0:
            print(f'\xa0{field[i-1]}\xa0\n', end='')
        else:
            print(f'\xa0{field[i-1]}\xa0|', end='')
    print()
    if char == "X":
        return winner(), "O"
    else:
        return winner(), "X"


def print_field():
    grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(1, 10):
        if i % 3 == 0:
            print(f' {grid[i-1]} \n', end='')
        else:
            print(f' {grid[i-1]} |', end='')
    print()


field = ['\xa0', '\xa0', '\xa0', '\xa0', '\xa0', '\xa0', '\xa0', '\xa0', '\xa0']

print("* Игровое поле с пронумерованными позициями *")
print_field()
char = 'X'
game_end = 0
while game_end == 0:
    game_end, char = turn(char, int(input(f"Выберите позицию для '{char}': ")))
    game_end, char = turn(char, int(input(f"Выберите позицию для '{char}': ")))




