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

#A
def A():
    s = S()
    t = S()
    ans = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            ans += 1
    print(ans)
    return

#B
def B():
    a,b = LI()
    for i in range(10000):
        if 1+i*a-i >= b:
            print(i)
            return
    return

#C
def C():
    n = I()
    a = LI()
    ans = 0
    r = 1
    for l in range(n):
        if r == l:
            r += 1
        while r < n and a[r-1] >= a[r]:
            r += 1
        ans = max(ans, r-l-1)
    print(ans)
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

#Solve
if __name__ == "__main__":
    C()
