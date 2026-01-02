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

    return

#C
def C():
    n = I()
    s = S()
    for i in range(2*n):
        s[i] = ord(s[i])-96
    k = 27
    m = 1<<n
    p = [1<<j for j in range(n)]
    d = defaultdict(lambda : 0)
    l = [(0,0)]
    for i in s[:n][::-1]:
        l = [(x[0]*k+i, x[1]) for x in l]+[(x[0], x[1]*k+i) for x in l]
    for i in l:
        d[i] += 1
    ans = 0
    l = [(0,0)]
    for i in s[n:]:
        l = [(x[0]*k+i, x[1]) for x in l]+[(x[0], x[1]*k+i) for x in l]
    for i in l:
        ans += d[i]
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
