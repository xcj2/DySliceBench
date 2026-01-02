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
    n = list(map(int, input()))
    l = len(n)
    dp = [[-float("inf")]*2 for i in range(l+1)]
    dp[0][0] = 0
    for i in range(l):
        ni = i+1
        for j in range(2):
            x = 9 if j else n[i]
            for d in range(x+1):
                nj = j|(d<n[i])
                c = dp[i][j]+d
                if dp[ni][nj] < c:
                    dp[ni][nj] = c
    print(max(dp[l]))
    return
#B
def B():

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

#F
def F():

    return

#Solve
if __name__ == "__main__":
    A()
