def examB():
    N = I()
    S = SI()
    cur = 0
    for i in range(N-1):
        d1 = set()
        d2 = set()
        for j in S[:i]:
            d1.add(j)
        for j in S[i:]:
            d2.add(j)
        curS = d1&d2
        cur = max(cur,len(curS))
    print(cur)


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

examB()
