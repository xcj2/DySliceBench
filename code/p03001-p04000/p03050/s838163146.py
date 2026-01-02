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

    return

#B
def B():
    n = I()

    return

#C
def C():
    n = I()

    return

#D
def D():
    def factorize(n):
        if n < 4:
            return [1,n]
        res = []
        for i in range(1,int(n**0.5)+1):
            if n%i == 0:
                res.append(i)
                if n//i != i:
                    res.append(n//i)
        res.sort()
        return res
    n = I()
    if n <= 2:
        print(0)
        quit()
    f = factorize(n)
    ans = 0
    for i in f:
        m = max(0,n//i-1)
        if i<m:
            ans += m
    print(ans)
    return

#E
def E():
    n = I()

    return

#F
def F():
    n = I()

    return

#G
def G():
    n = I()

    return

#H
def H():
    n = I()

    return

#I
def I_():
    n = I()

    return

#J
def J():
    n = I()

    return

#Solve
if __name__ == "__main__":
    D()
