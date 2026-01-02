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


def count_cost(xy: list, p: int, q: int):
    n = len(xy)
    cnt = n

    for xi, yi in xy:
        if [xi+p, yi+q] in xy:
            cnt -= 1

    return cnt


n = ni()
xy = [list(li()) for _ in range(n)]

ans = n
for i in range(n):
    for j in range(i+1, n):
        xi, yi = xy[i]
        xj, yj = xy[j]

        p, q = xj - xi, yj - yi

        ans = min(ans, count_cost(xy, p, q))

print(ans)