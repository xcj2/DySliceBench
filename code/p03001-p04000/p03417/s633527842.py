def examC():
    NM = LI(); NM.sort()
    if NM[0]>=2:
        ans = (NM[0]-2)*(NM[1]-2)
    else:
        if NM[1]==1:
            ans = 1
        else:
            ans = max(0,NM[1]-2)
    print(ans)


import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()