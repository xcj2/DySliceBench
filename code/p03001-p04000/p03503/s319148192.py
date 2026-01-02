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
    n = I()
    f = LIR(n)
    po = [1]*11
    for i in range(n):
        k = 0
        p = 1
        for j in range(10):
            k += p*f[i][j]
            p *= 2
            po[j+1] = p
        f[i] = k
    p = LIR(n)
    ans = -float("inf")
    for i in range(1,1024):
        k = 0
        for j in range(n):
            c = i&f[j]
            s = 0
            for l in po:
                if c&l:s += 1
            k += p[j][s]
        ans = max(ans,k)
    print(ans)
#D
def D():
    n,C = LI()
    T = [[0 for i in range(200002)] for j in range(C)]
    for i in range(n):
        s,t,c = LI()
        c -= 1
        T[c][2*s] += 1
        T[c][2*t+1] -= 1
    for c in range(C):
        for i in range(200000):
            T[c][i+1] += T[c][i]
    ans = 0
    for i in range(200000):
        k = 0
        for c in range(C):
            if T[c][i]:k += 1
        ans = max(ans, k)
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
    C()
