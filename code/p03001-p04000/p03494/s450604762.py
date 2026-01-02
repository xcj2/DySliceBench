def examB():
    N = I()
    A = LI()
    cur = -1
    flag=True
    while(flag):
        for i in range(N):
            if A[i]%2==1:
                flag = False
                break
            A[i]=A[i]//2
        cur +=1
    print(cur)

import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
