from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
#from math import *
from collections import defaultdict as dd, deque
def data(): return sys.stdin.readline().strip()
def mdata(): return map(int, data().split())
out=sys.stdout.write
#sys.setrecursionlimit(100000)
INF=int(10e9)


def knapSack(V):
    for i in range(n + 1):
        for v in range(V + 1):
            if v == 0:
                K[i][v] = 0
            elif val[i - 1] <= v:
                K[i][v] = min(wt[i - 1] + K[i - 1][v - val[i - 1]], K[i - 1][v])
            else:
                K[i][v] = K[i - 1][v]

    return K[n][V]

n,w=mdata()
val=[0]*(n)
wt=[0]*(n)
for i in range(n):
    wt[i],val[i]=mdata()
V=100005
K = [[1000000007 for x in range(V + 1)] for x in range(n + 1)]
knapSack(V)
m=0
for i in range(n + 1):
    for v in range(V + 1):
        if 1<=K[i][v]<=w :
            m=max(m,v)
print(m)
