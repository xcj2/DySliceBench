def examC():
    N = I()
    ans = "Yes"
    now = [0,0,0]
    for _ in range(N):
        t, x, y = LI()
        T = t - now[0]
        X = x - now[1]
        Y = y - now[2]
        if abs(X)+abs(Y)>T or (abs(X)+abs(Y)-T)%2==1:
            ans = "No"
            break
        else:
            now = [t,x,y]
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
