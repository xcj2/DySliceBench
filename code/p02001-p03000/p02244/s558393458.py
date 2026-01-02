from enum import Enum, auto
class Square(Enum):
    FREE = auto()
    NOT_FREE = auto()

row = [Square.FREE for i in range(8)]
col = [Square.FREE for i in range(8)]
dpos = [Square.FREE for i in range(2*8-1)]
dneg = [Square.FREE for i in range(2*8-1)]

board = [[False for j in range(8)] for i in range(8)]

def set_board(r, c, v=True):
    global board
    if v:
        board[r][c] = True
        row[r] = Square.NOT_FREE
        col[c] = Square.NOT_FREE
        dpos[r+c] = Square.NOT_FREE
        dneg[r-c+8-1] = Square.NOT_FREE
    else:
        board[r][c] = False
        row[r] = Square.FREE
        col[c] = Square.FREE
        dpos[r+c] = Square.FREE
        dneg[r-c+8-1] = Square.FREE

def print_board():
    for i in range(8):
        for j in range(8):
            if board[i][j]:
                print('Q', end='')
            else:
                print('.', end='')
        print('')

def recursive(i): # i はrow番号
    global board, row, col, dpos, dneg
    if i == 8:
        print_board()
        return None

    if row[i] == Square.NOT_FREE:
        recursive(i+1)
    else:
        for j in range(8):
            if col[j] == Square.NOT_FREE or dpos[i+j] == Square.NOT_FREE or dneg[i-j+8-1] == Square.NOT_FREE:
                continue
            set_board(i, j, True)
            recursive(i+1)
            set_board(i, j, False)

k = int(input())
for i in range(k):
    r, c = list(map(int, input().split(' ')))
    set_board(r, c, True)
recursive(0)

