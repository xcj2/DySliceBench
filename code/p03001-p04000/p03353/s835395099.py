def examC():
    S = SI()
    K = I()
    d = set()
    for i in range(len(S)):
        for j in range(5):
            s = S[i:(i+j+1)]
            d.add(s)
    d = list(d)
    d.sort()
    print(d[K-1])

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
