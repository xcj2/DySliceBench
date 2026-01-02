#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

n = I()
a = LI()
b = LI()
s = 0
for i in range(n):
    if a[i] < b[i]:
        k = b[i]-a[i]
        k += k&1
        s += (k>>1)
        a[i] += k
for i in range(n):
    if b[i] < a[i]:
        k = a[i]-b[i]
        if s < k:
            print("No")
            quit()
        b[i] += k
        s -= k
print("Yes")
