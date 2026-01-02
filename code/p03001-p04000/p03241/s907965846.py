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
sys.setrecursionlimit(1000000)

#A
def A():
    return

#B
def B():
    return

#C
def C():
    n = I()
    a = LIR(n)
    if n == 1:
        print(*a[0])
        quit()
    for cy in range(101):
        for cx in range(101):
            for i in range(n):
                x,y,h = a[i]
                if h > 0:
                    H = abs(x-cx)+abs(y-cy)+h
                    break
            f = True
            for i in range(n):
                x,y,h = a[i]
                if max(H-abs(x-cx)-abs(y-cy),0) != h:
                    f = False
                    break
            if f:
                print(cx,cy,H)
                quit()
#D
def D():
    def factorize(n):
        if n == 1:
            return [1]
        if n<4:
            return [1,n]
        l = [1,n]
        m = n
        z = 2
        while z**2 <= n:
            if m%z == 0:
                l.append(z)
                if m//z != z:
                    l.append(m//z)
            z += 1
        l = list(set(l))
        l.sort()
        return l

    n,m = LI()
    l = factorize(m)
    for i in l[::-1]:
        if n*i <= m:
            print(i)
            quit()

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
