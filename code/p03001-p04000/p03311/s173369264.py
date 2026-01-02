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
if n == 1:
    print(0)
    quit()
for i in range(n):
    a[i] -= i+1
a.sort()
b = a[n>>1]
ans = 0
for i in a:
    ans += abs(i-b)
if n%2:
    b = a[(n>>1)+1]
    ans_ = 0
    for i in a:
        ans_ += abs(i-b)
    if ans > ans_:
        ans = ans_
    b = (a[(n>>1)+1]+a[n>>1])>>1
    ans_ = 0
    for i in a:
        ans_ += abs(i-b)
    if ans > ans_:
        ans = ans_
print(ans)
