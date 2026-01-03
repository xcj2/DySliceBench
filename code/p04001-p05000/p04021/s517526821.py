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

    return

#B
def B():
    n = I()
    a = IR(n)
    ans = 0
    b = [0]*(n+1)
    for i in range(n):
        ans += (a[i]+b[i])>>1
        if (a[i]%2)^(b[i]%2) and a[i]:
            b[i+1] += 1
    print(ans)
    return

#C
def C():
    n = I()
    a = IR(n)
    b = [(a[i],i) for i in range(n)]
    b.sort()
    for i in range(n):
        a[b[i][1]] = i+1
    ans = 0
    for i in range(n):
        if a[i]&1 == i&1:
            ans += 1
    print(ans>>1)
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
