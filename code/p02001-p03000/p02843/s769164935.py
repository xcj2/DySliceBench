def examC():
    X = I()
    p,q = divmod(X,100)
    if q>p*5:
        ans = 0
    else:
        ans = 1
    print(ans)
    return

def examD():
    return
def examE():
    return

def examF():
    return

import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
