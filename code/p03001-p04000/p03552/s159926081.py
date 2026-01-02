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
    n,k = LI()
    a = LI()
    d = defaultdict(lambda:0)
    for i in a:
        d[i] += 1
    d = list(d.values())
    d.sort()
    ans = 0
    for i in range(len(d)-k):
        ans += d[i]
    print(ans)
    return

#B
def B():
    n,z,w = LI()
    a = LI()
    if n == 1:
        print(abs(a[0]-w))
        return
    ans = max(abs(a[-1]-w),abs(a[-2]-a[-1]))
    print(ans)
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

#Solve
if __name__ == "__main__":
    B()
