
def examB():
    N = I()
    S = SI()
    lim = ord("Z")
    ans = ""
    for s in S:
        cur = ord(s)+N
        if cur>lim:
            cur -=26
        ans += chr(cur)
    print(ans)
    return

def examC():
    return

def examD():
    return

def examE():
    return

def examF():
    return

import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
