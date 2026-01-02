#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    s = S()
    for i in range(3):
        if s[i] == s[i + 1]:
            print("Bad")
            return
    print("Good")
    return

#B
def B():
    n, l = LI()
    lis = [l + i for i in range(n)]
    s = sum(lis)
    a = inf
    for i in lis:
        if abs(a) > abs(i):
            a = i
    print(s-a)
    return

#C
def C():
    def gcd(a, b):
        a, b = max(a, b), min(a, b)
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b // gcd(a, b)
    a, b, c, d = LI()
    x = b // c - (a-1) // c
    y = b // d - (a-1) // d
    z = b // lcm(c , d) - (a-1) // lcm(c , d)
    print(b-a+1-(x+y-z))
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
if __name__ == '__main__':
    B()
