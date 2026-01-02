def examB():
    N = I()
    max_N = 50001
    origin = [None]*int(max_N*1.08+10)
    for i in range(max_N):
        origin[int(i*1.08)] = i
    if origin[N]:
        ans = origin[N]
    else:
        ans = ":("
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
