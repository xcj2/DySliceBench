def examB():
    N, M = LI()
    cur = [0]*N
    for i in range(M):
        a, b = LI()
        cur[a-1] +=1
        cur[b-1] +=1
    ans = "YES"
    for j in cur:
        if j%2==1:
            ans = "NO"
            break
    print(ans)


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
