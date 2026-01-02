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
a = list(li())

absmin = 10**18
mnscnt = 0
ans = 0

for ai in a:
    if ai < 0:
        mnscnt += 1

    absmin = min(absmin, abs(ai))
    ans += abs(ai)

if mnscnt % 2:
    print(ans - 2*absmin)
else:
    print(ans)