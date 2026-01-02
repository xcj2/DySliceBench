def examC():
    N = I()
    a = LI()
    d = defaultdict(int)
    for i in a:
        d[i] +=1
    cur = 0
    for i,j in d.items():
        if i==j:
            continue
        elif i<j:
            cur += (j-i)
        else:
            cur +=j
    print(cur)


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
