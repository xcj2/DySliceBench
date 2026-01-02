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
    n = I()
    ans = float("inf")
    for i in range(n+1):
        m = 0
        k = i
        while k > 0:
            m += k%6
            k //= 6
        k = n-i
        while k > 0:
            m += k%9
            k //= 9
        if m < ans:
            ans = m
    print(ans)
    return

#B
def B():
    n = I()
    x = [None for i in range(n)]
    y = [None for i in range(n)]
    h = [None for i in range(n)]
    for i in range(n):
        x[i],y[i],h[i] = LI()
    if n == 1:
        print(x[0],y[0],h[0])
        quit()
    for cy in range(101):
        for cx in range(101):
            for i in range(n):
                if h[i] > 0:break
            ch = h[i]+abs(x[i]-cx)+abs(y[i]-cy)
            f = 1
            for i in range(n):
                if max(ch-abs(x[i]-cx)-abs(y[i]-cy),0) != h[i]:f = 0
            if f:
                print(cx,cy,ch)
                quit()
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

#I
def I_():
    return

#J
def J():
    return

#Solve
if __name__ == "__main__":
    B()
