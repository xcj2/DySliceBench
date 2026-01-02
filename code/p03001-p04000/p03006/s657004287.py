def examB():
    N = I()
    X = [0]*N; Y = [0]*N
    for i in range(N):
        X[i],Y[i] = LI()
    pq = defaultdict(int)
    for i in range(N):
        for j in range(i+1,N):
            curx = X[j]-X[i]
            cury = Y[j]-Y[i]
            pq[curx,cury] +=1
            pq[-curx, -cury] += 1
    if N>1:
        ans = N - max(pq.values())
    else:
        ans = 1
    print(ans)

from string import digits
import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
