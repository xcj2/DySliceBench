import sys
from collections import Counter
from collections import deque
import heapq
import math
import fractions
import bisect
import itertools
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))


n=10
h,w=mp()
d=[lmp() for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j],d[i][k] + d[k][j])
ans=0
for i in range(h):
    l=lmp()
    for k in range(w):
        if l[k]!=-1:
            ans+=d[l[k]][1]
print(ans)