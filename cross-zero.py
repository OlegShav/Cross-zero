def rules():
    print("Добро пожаловать в игру Крестики-нолики!")
    print("Для осуществления хода введите координаты поля в формате x y, где:"
          "x - номер строки y - номер столбца")

field = [[" "] * 3 for i in range(3)]
def board():
    print(f"      0   1   2")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)

def step():
    while True:
        cords = input("Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue
        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числовые координаты!")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона поля!")
            continue
        if field[x][y] != " ":
            print("Клетка занята, переходите!")
            continue
        return x, y

def win_check():
    win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cords:
        symb = []
        for с in cord:
            symb.append(field[с[0]][с[1]])
        if symb == ["X", "X", "X"]:
            print("Крестик выиграл! Поздравляю")
            return True
        if symb == ["O", "O", "O"]:
            print("Нолик выиграл! Поздравляю")
            return True
    return False

rules()

count = 0
while True:
    count += 1
    board()
    if count % 2 == 1:
        print("Ход крестика")
    else:
        print("Ход нолика")

    x, y = step()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if win_check():
        break
    if count == 9:
        print("Победила дружба!")
        break