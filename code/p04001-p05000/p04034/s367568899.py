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

n, m = li()
balls = [1]*n
canex = [0]*n

canex[0] = 1

for _ in range(m):
    x, y = li_()
    balls[x] -= 1
    balls[y] += 1

    if balls[x] > 0 and canex[x]:
        canex[y] = 1

    elif balls[x] == 0 and canex[x]:
        canex[y] = 1
        canex[x] = 0

print(sum(canex))