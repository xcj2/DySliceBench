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

n = ni()
a = list(li())

a.sort()

cum = list(accumulate(a))

ans = 1

for i in range(len(a) - 2, -1, -1):
    if a[i+1] > 2*cum[i]:
        break

    ans += 1

print(ans)
