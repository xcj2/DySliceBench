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


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

n,w=mdata()
val=[0]*(n)
wt=[0]*(n)
for i in range(n):
    wt[i],val[i]=mdata()
print(knapSack(w,wt,val,n))