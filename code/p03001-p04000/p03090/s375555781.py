def examB():
    N = I()
    M = (N-1)**2//2
    ans = []
    for i in range(1,N+1):
        if N%2==0:
            for j in range(i+1,N+1):
                if i+j!=N+1:
                    ans.append([i,j])
        else:
            for j in range(i+1,N):
                if i+j!=N:
                    ans.append([i,j])
            if i!=N:
                ans.append([i,N])
    print(M)
    for v in ans:
        print(" ".join(map(str,v)))

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
