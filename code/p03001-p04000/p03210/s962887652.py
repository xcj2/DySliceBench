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
    x = I()
    if x in [3,5,7]:
        print("YES")
    else:
        print("NO")
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
    def factorial(n):
        if n <= 3:
            return [n]
        l = []
        i = 2
        m = n
        while i**2 <= n:
            while m%i == 0:
                l.append(i)
                m //= i
            i += 1
        if m != 1:
            l.append(m)
        return l

    n = I()
    d = defaultdict(int)
    for i in range(2,n+1):
        l = factorial(i)
        for j in l:
            d[j] += 1
    a3 = 0
    a5 = 0
    a15 = 0
    a25 = 0
    a75 = 0
    for i in d.keys():
        if d[i] >= 74:
            a75 += 1
        if d[i] >= 24:
            a25 += 1
        if d[i] >= 14:
            a15 += 1
        if d[i] >= 4:
            a5 += 1
        if d[i] >= 2:
            a3 += 1
    ans = a75+(a3-1)*a25+(a5-1)*a15+(a3-2)*a5*(a5-1)//2
    print(ans)
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
    A()
