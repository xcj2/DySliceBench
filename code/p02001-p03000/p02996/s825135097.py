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

n = ni()
ab = [list(li()) for _ in range(n)]

ab.sort(key=lambda x: x[1])

cur = 0

ans = True

for ai, bi in ab:
    cur += ai
    if cur > bi:
        ans = False

print("Yes" if ans else "No")