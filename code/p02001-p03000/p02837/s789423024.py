import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush,heapify
sys.setrecursionlimit(10**6)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7

n = INT()
ll = [[] for _ in range(n)]
l = [0]*n

for i in range(n):
    tmp = INT()
    for j in range(tmp):
        x,y = MAP()
        ll[i].append([x-1,y])

ans = 0
for bit in range(2**n):
    ok = True
    is_honest = [(bit>>i) & 1 for i in range(n)]
    #print(is_honest)
    for i in range(n):
        if not is_honest[i]:
            continue
        for x,y in ll[i]:
            if is_honest[x]!=y:
                ok=False
    if ok:
        ans = max(ans,sum(is_honest))
print(ans)