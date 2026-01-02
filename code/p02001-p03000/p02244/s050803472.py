import sys
import time
input = sys.stdin.readline
FREE = True
NOT_FREE = False

num = int(input())
Q = [list(map(int, input().split())) for i in range(num)]

row = [FREE]*8
col = [FREE]*8
dpos = [FREE]*15
dneg = [FREE]*15
chess_board = [['.' for i in range(8)] for j in range(8)]

def printBoard():
    for c in chess_board:
        print("".join(c))

def chess_init():
    for q in Q:
        i = q[0]
        j = q[1]
        chess_board[i][j] = 'Q'
        row[i] = col[j] = dpos[i+j] = dneg[i-j+7] = NOT_FREE

def putQueen(i):

    if(i == 8):
        printBoard()
        return
    
    row_idx = 0
    for j in range(8):
        if(row[j] == FREE):
            row_idx = j
            break

    for j in range(8):
        if(col[j] == NOT_FREE or dpos[row_idx+j] == NOT_FREE or dneg[row_idx-j+7] == NOT_FREE):
            continue
        # not free jya nai nara oku
        chess_board[row_idx][j] = 'Q'
        row[row_idx] = col[j] = dpos[row_idx+j] = dneg[row_idx-j+7] = NOT_FREE
        putQueen(i+1)
        # i+1 banme tansaku site kokoni kaette kitara
        # tansaku sippai = backtracking suru kara FREE ni modosu
        chess_board[row_idx][j] = '.'
        row[row_idx] = col[j] = dpos[row_idx+j] = dneg[row_idx-j+7] = FREE

if __name__ == "__main__":
    chess_init()
    # sudeni okareta koma igai no koma no tansaku suru
    putQueen(num)




