import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

from itertools import combinations

N,M,Q = LI()
a,b,c,d = LIR(Q,4)

X = list(combinations(range(N+M-1),M-1))

ans = 0
for x in X:
    s = 0
    L = []
    for x0 in x:
        L.append(x0-s)
        s = x0+1
    L.append(N+M-1-s)
    now = []
    for i in range(len(L)):
        now.extend([i+1]*L[i])
    val = 0
    for i in range(Q):
        if now[b[i]-1]-now[a[i]-1] == c[i]:
            val += d[i]
    if val > ans:
        ans = val

print(ans)