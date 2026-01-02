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


l, r = li()
MOD = 2019

ans = float("inf")
if r-l >= 2018:
    ans = 0
else:
    for i in range(l, min(r+1, l+2*MOD)):
        for j in range(i+1, min(r+1, l+2*MOD)):
            ans = min(ans, i*j % MOD)

print(ans)