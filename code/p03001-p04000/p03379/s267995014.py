def examC():
    N = I()
    x = LI(); num = [i for i in range(N)]
    X = list(zip(x,num)); X.sort()
    ans = [0]*N
    mid0 = X[(N)//2-1][0]; mid1 = X[(N)//2][0]
    for i in range(N):
        if X[i][0]<mid1:
            ans[X[i][1]] = mid1
        else:
            ans[X[i][1]] = mid0
    for v in ans:
        print(v)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
