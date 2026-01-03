def examD():
    N = I()
    St = S()
    cur = 0
    left = 0; right = 0
    for s in St:
        if s=="(":
            cur +=1
        if s==")":
            if cur>0:
                cur -=1
            else:
                left +=1
    right = cur
    ans = "("*left + St + ")"*right
    print(ans)

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

examD()
