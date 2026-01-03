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
    s = LI()
    if sum(s) ==  2*max(s):
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    w,h,n = LI()
    l,r = 0,w
    d,u = 0,h
    for i in range(n):
        x,y,a = LI()
        if a == 1:
            l = max(x,l)
        elif a == 2:
            r = min(x,r)
        elif a == 3:
            d = max(y,d)
        else:
            u = min(y,u)
    print(max(r-l,0)*max(u-d,0))
    return

#C
def C():
    return

#D
def D():
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
    B()
