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
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007

#A
def A():
    return

#B
def B():
    return

#C
def C():
    n = list(map(int,S()))
    l = len(n)
    dp = [[[0 for k in range(16)] for j in range(2)] for i in range(l+1)]
    dp[0][0][0] = 1
    for i in range(l):
        for j in range(2):
            for k in range(9):
                x = 9 if j else n[i]
                for d in range(x+1):
                    if d == 3:
                        f = 1
                    elif d == 5:
                        f = 2
                    elif d == 7:
                        f = 4
                    else:
                        if k == 0 and d == 0:
                            f = 0
                        else:
                            f = 8
                    dp[i+1][j or d < n[i]][k|f] += dp[i][j][k]
    ans = 0
    for i in range(2):
        ans += dp[l][i][7]
    print(ans)
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
if __name__ == "__main__":
    C()
