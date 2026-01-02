import sys
# sys.stdin = open('input.txt')

def print_board(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] and row[i] != j:
                return
    for i in range(n):
        for j in range(n):
            if row[i] == j:
                print('Q', end='')
            else:
                print('.', end='')
        print('')

def set_queen(i, j):
    row[i] = j
    col[j] = NOT_FREE
    dpos[i+j] = NOT_FREE
    dneg[i-j+n-1] = NOT_FREE

def remove_queen(i, j):
    row[i] = FREE
    col[j] = FREE
    dpos[i+j] = FREE
    dneg[i-j+n-1] = FREE

def recursive(i):
    if i == n:
        print_board(board)
        return
    for j in range(n):
        if col[j] == NOT_FREE or dpos[i+j] == NOT_FREE or dneg[i-j+n-1] == NOT_FREE:
            continue
        set_queen(i, j)
        recursive(i+1)
        # 以下の行は、i+1 行目にクイーンを配置できなかったときのみ実行される
        remove_queen(i, j)
    # for を最後まで実行できた場合、クイーンの配置ができなかったことになる (i 行目についてすべての列 (j) を試したが NG)


n = 8
FREE = -1
NOT_FREE = 1

col = []
row = []
dpos = []
dneg = []
board = [[False] * n for i in range(n)]

for i in range(n):
    col.append(FREE)
    row.append(FREE)
for i in range(2 * n - 1):
    dpos.append(FREE)
    dneg.append(FREE)

k = int(input())
for i in range(k):
    r, c = map(int, input().split())
    board[r][c] = True

recursive(0)
