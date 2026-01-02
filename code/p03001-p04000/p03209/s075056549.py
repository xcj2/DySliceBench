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
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007

#A
def A():
    return

#B
def B():
    return

#C
def C():
    n,k = LI()
    h = IR(n)
    h.sort()
    ans = float("inf")
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

#D
def D():
    n,x = LI()
    l = [1 for i in range(n+1)]
    for i in range(n):
        l[i+1] = 2*l[i]+3
    p = [1 for i in range(n+1)]
    for i in range(n):
        p[i+1] = 2*p[i]+1
    ans = 0
    for i in range(1,n+1)[::-1]:
        if i == 1:
            if x == 5:ans += 3
            else:ans += max(0,x-1)
        else:
            if x == 0:continue
            if x == l[i]:
                ans += p[i]
                x = 0
            if x > l[i-1]+1:
                ans += p[i-1]+1
                x -= l[i-1]+2
            else:
                x -= 1
    print(ans)
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
