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

from collections import Counter

n,m = li()
a = list(li())

acum = [0]

for ai in a:
    acum.append((acum[-1] + ai) % m)

cnts = Counter(acum)
ans = 0
for key, val in cnts.items():
    ans += (val-1)*val // 2

print(ans)


