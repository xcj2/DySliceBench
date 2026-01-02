# coding:utf-8

import sys
from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, m = LI()
YP = [[y, p] for p, y in (LI() for _ in range(m))]

YP2 = sorted(YP)

P = defaultdict(int)
ans = {}
for y, p in YP2:
    P[p] += 1
    l1, l2 = len(str(p)), len(str(P[p]))
    id = (6 - l1) * '0' + str(p) + (6 - l2) * '0' + str(P[p])
    ans[y] = id

for y, p in YP:
    print(ans[y])
