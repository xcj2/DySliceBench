def examC():
    N = I()
    a = LI()
    d = defaultdict(int)
    for i in a:
        d[min(i//400,8)] += 1
    ansL = len(d)
    ansR = len(d)
    if d[8]!=0:
        ansL = max(ansL-1,1)
        ansR = ansR + d[8]-1
    print(ansL, ansR)


import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()