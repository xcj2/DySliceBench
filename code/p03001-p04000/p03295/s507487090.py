# Input
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

n,m = li()
ab = []
for _ in range(m):
    ai, bi = li_()
    ab.append((ai, bi))

ab.sort(key=lambda x: x[1])

ans = 0
cur = -1
for ai, bi in ab:
    if ai >= cur:
        ans += 1
        cur = bi

print(ans)


