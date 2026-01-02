import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


def cum_2d(field: list):
    row = len(field)
    col = len(field[0])

    # 横方向に累積和
    for r in range(row):
        for c in range(col - 1):
            field[r][c + 1] += field[r][c]

    # 縦方向に累積和
    for c in range(col):
        for r in range(row - 1):
            field[r + 1][c] += field[r][c]

    return field

n,m,q = li()
field = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    l, r = li()
    field[l][r] += 1

field = cum_2d(field)

for _ in range(q):
    pi, qi = li()
    print(field[qi][qi] - field[qi][pi-1] - field[pi-1][qi] + field[pi-1][pi-1])