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


n, d = li()
x = [list(li()) for _ in range(n)]

SQUARE = set([i * i for i in range(10000)])
ans = 0

for i in range(n):
    for j in range(i+1, n):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k])**2

        if dist in SQUARE:
            ans += 1

print(ans)
