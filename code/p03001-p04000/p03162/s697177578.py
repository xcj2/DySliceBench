#!usr/bin/env python3
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

#A
def A():
    n = II()
    h = LI()
    dp = [0 for i in range(n)]
    dp[1] = abs(h[0] - h[1])
    for i in range(2,n):
        dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i]), dp[i - 2] + abs(h[i - 2] - h[i]))
    print(dp[n-1])
    return

#B
def B():
    n, K = LI()
    h = LI()
    dp = [float("INF") for i in range(n + K + 1)]
    dp[0] = 0
    for i in range(n):
        for k in range(1, K + 1):
            if i + k >= n:
                break
            dp[i + k] = min(dp[i + k], dp[i] + abs(h[i] - h[i + k]))
    print(dp[n-1])
    return

#C
def C():
    n = II()
    abc = LIR(n)
    dp = [0 for i in range(3 * n + 1)]
    dp[0] = abc[0][0]
    dp[1] = abc[0][1]
    dp[2] = abc[0][2]
    for i in range(1,n):
        dp[3 * i] = max(dp[3 * i], dp[3 * (i - 1) + 1] + abc[i][0], dp[3 * (i - 1) + 2] + abc[i][0])
        dp[3 * i + 1] = max(dp[3 * i + 1], dp[3 * (i - 1) + 2] + abc[i][1], dp[3 * (i - 1)] + abc[i][1])
        dp[3 * i + 2] = max(dp[3 * i + 2], dp[3 * (i - 1) + 1] + abc[i][2], dp[3 * (i - 1)] + abc[i][2])
    dp[3 * n] = max(dp)
    print(dp[3*n])

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

#I
def I():
    return 
#J

#K

#L

#M
#N
# O
# P
# Q
# R
# S
# T
# U
# V
# W
# X
# Y
# Z


#Solve
if __name__ == '__main__':
    C()
