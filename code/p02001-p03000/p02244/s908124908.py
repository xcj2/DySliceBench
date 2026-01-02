import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
col = []
row = []
rd = []
lu = []
board = [['.'] * 8 for _ in range(8)]

def put(r, c):
    global col, row, rd, lu, board
    col.append(c)
    row.append(r)
    rd.append(c-r)
    lu.append(r+c)
    board[r][c] = 'Q'

def canPut(i, j):
    if i not in row and j not in col and j-i not in rd and i+j not in lu:
        return True
    else:
        return False

def unput(i, j):
    global col, row, rd, lu, board
    col.remove(j)
    row.remove(i)
    rd.remove(j-i)
    lu.remove(i+j)
    board[i][j] = '.'

def rec(i):
    if i > 7:
        for p in range(8):
            print(''.join(board[p]))
        exit(0)
    # print("i: ", i)
    for j in range(8):
        if canPut(i, j):
            put(i, j)
            # print("put: ", i, j)
            k = i+1
            while k in row:
                k += 1
            rec(k)
            unput(i, j)

def main():
    global col, row, rd, lu
    n = int(input().strip())

    for i in range(n):
        r, c = list(map(int, input().strip().split()))
        put(r, c)
    k = 0
    while k in row:
        k += 1
    rec(k)


if __name__ == '__main__':
    main()

