def examC(inf):
    N = I()
    A = LI()
    sumA = [0]*N
    sumA[0] = A[0]
    cur = inf
    for i in range(N-1):
        sumA[i+1] = sumA[i]+A[i+1]
    for i in range(N-1):
        if cur>abs(sumA[N-1]-sumA[i]*2):
            cur = abs(sumA[N-1]-sumA[i]*2)
    ans = cur
    print(ans)


import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC(inf)
