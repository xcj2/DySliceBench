import sys,math,itertools,bisect,copy,re

from collections import Counter, deque, defaultdict
from itertools import accumulate, permutations, combinations, takewhile, compress, cycle
from functools import reduce
from math import ceil, floor, log10, log2, factorial
from pprint import pprint
# 10倍速いらしい
input = sys.stdin.readline

INF = float('inf')
MOD = 10**9+7
EPS = 10**-7
sys.setrecursionlimit(1000000)

# N = int(input())
# N,M = [int(x) for x in input().split()]
# V = [[0] * 100 for _ in range(100)]
# A = [int(input()) for _ in range(N)]
# DP = [[0] * 100 for _ in range(100)]
# DP = defaultdict(lambda: float('inf'))

N,M = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]


# Union Find
# N = 100
PARENT = list(range(N))

def root(n):
    if PARENT[n] == n:
        return n
    else:
        ret = root(PARENT[n])
        PARENT[n] = ret
        return ret

def same(n1, n2):
    return root(n1) == root(n2)

def unite(n1, n2):
    n1 = root(n1)
    n2 = root(n2)
    if n1 == n2:
        return
    PARENT[n1] = n2

for _ in range(M):
    x, y = [int(x) for x in input().split()]
    x -= 1
    y -= 1
    unite(x,y)

# print(PARENT)

D1 = dict()
D2 = dict()

for i in range(N):
    grp = root(i)
    s1 = D1.get(grp, set())
    s1.add(i+1)
    D1[grp] = s1

    s2 = D2.get(grp, set())
    s2.add(P[i])
    D2[grp] = s2

# print(D1)
# print(D2)

ans = 0
for grp in set(PARENT):
    s1 = D1.get(grp, set())
    s2 = D2.get(grp, set())
    ans += len(s1 & s2)

print(ans)
    

    
