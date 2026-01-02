#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    return

#B
def B():
    return

#C
def C():
    return

#D
def D():
    n = I()
    a = LI()
    for i in range(n-1):
        a[i+1] += a[i]
    a.insert(0,0)
    ans = float("inf")
    for m in range(3,n):
        lu = a[m-1]
        ru = a[n]-a[m-1]
        lm = bisect.bisect_left(a,lu//2)
        rm = bisect.bisect_left(a,ru//2+a[m-1])
        k = [a[lm],a[m-1]-a[lm],a[rm]-a[m-1],a[n]-a[rm]]
        if min(k):
            ans = min(ans,max(k)-min(k))
        lm -= 1
        k = [a[lm],a[m-1]-a[lm],a[rm]-a[m-1],a[n]-a[rm]]
        if min(k):
            ans = min(ans,max(k)-min(k))
        rm -= 1
        k = [a[lm],a[m-1]-a[lm],a[rm]-a[m-1],a[n]-a[rm]]
        if min(k):
            ans = min(ans,max(k)-min(k))
        lm += 1
        k = [a[lm],a[m-1]-a[lm],a[rm]-a[m-1],a[n]-a[rm]]
        if min(k):
            ans = min(ans,max(k)-min(k))
    print(ans)
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == "__main__":
    D()
