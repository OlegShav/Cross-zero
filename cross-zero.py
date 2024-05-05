field = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
def board():
    print(f" 0 1 2")
    for i in range(3):
        row = " ".join(field[i])
        print(f"{i} {row}")

def step_input(player):
    pass
def win_check():
    pass
def start():
    pass

board()