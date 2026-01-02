def changeBoard(board, i, j, d):
    n = 8
    for k in range(n):
        board[i][k] += d
        board[k][j] += d
    if i > j:
        for k in range(n - i + j):
            board[k + i - j][k] += d
    else:
        for k in range(n - j + i):
            board[k][k + j - i] += d
    if i + j < n:
        for k in range(i + j):
            board[i + j -k][k] += d
    else:
        for k in range(i + j - n + 1, n):
            board[i + j -k][k] += d

def checkQueen(queen, initial):
    for r in initial.keys():
        if queen[r] != initial[r]:
            return False
    return True

def printQueen(queen):
    for c in queen:
        line = list("........")
        line[c] = "Q"
        print("".join(line))

def setQueen(queen, board, i, initial):
    n = 8
    if i == n:
        if checkQueen(queen, initial):
            printQueen(queen)
        return
    for j in range(n):
        if board[i][j] == 0:
            queen[i] = j
            changeBoard(board, i, j, 1)
            setQueen(queen, board, i + 1, initial)
            changeBoard(board, i, j, -1)

b = [[0 for i in range(8)] for j in range(8)]
q = [-1 for i in range(8)]
q_ini = {}

k = int(input())
for i in range(k):
    r, c = map(int, input().split())
    q[r] = c
    q_ini[r] = c

setQueen(q, b, 0, q_ini)