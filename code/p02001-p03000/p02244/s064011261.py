import sys
N = 8
board = [[0 for j in range(N)] for i in range(N)]
queen = [-1] * N

def main():
    init()
    search(0)

def search(i):
    if i == N:
        printBoard()
        sys.exit()
    
    if queen[i] != -1:
        search(i + 1)

    else :
        for j in range(N):
            if board[i][j] == 0:
                queen[i] = j
                changeBoard(i, j, 1)
                search(i + 1)
                changeBoard(i, j, -1)
                queen[i] = -1

def init():
    k = int(input())

    for i in range(k):
        a = list(map(int, input().split()))
        queen[a[0]] = a[1]
        changeBoard(a[0], a[1], 1)

def changeBoard(i, j, number):
    for k in range(N):
        board[i][k] += number
        board[k][j] += number

    if i > j :
        for k in range(N - (i - j)) :
            board[k + (i - j)][k] += number
    else:
        for k in range(N - (j - i)) :
            board[k][k + (j - i)] += number
    if i + j < N :
        for k in range(i + j + 1) :
            board[i + j - k][k] += number
    else:
        for k in range(i + j - N + 1, N):
            board[i + j - k][k] += number

def printBoard():
    for i in range(N):
        for j in range(N):
            if queen[i] == j:
                print('Q' ,end = "")
            else:
                print('.' ,end = "")
        print()

if __name__ == '__main__':
    main()
