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
ab = [tuple(li()) for _ in range(n)]

ab.sort(key=lambda x: x[1])
cur = 0
ok = True

for ai, bi in ab:
    cur += ai
    if cur > bi:
        ok = False
        break

print("Yes" if ok else "No")
