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

from itertools import accumulate

n ,m = li()

imos = [0]*(n+1)

for _ in range(m):
    l,r = li_()
    imos[l] += 1
    imos[r+1] -= 1

cum = list(accumulate(imos))

ans = 0
for ci in cum:
    if ci == m:
        ans += 1

print(ans)