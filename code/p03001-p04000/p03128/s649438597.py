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
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    a,b = LI()
    if b%a == 0:
        print(a+b)
    else:
        print(b-a)
    return

#B
def B():
    n,m = LI()
    d = defaultdict(int)
    for i in range(n):
        l = LI()
        for j in range(1,len(l)):
            d[l[j]] += 1
    ans = 0
    for i in d.values():
        if i == n:
            ans += 1
    print(ans)
    return

#C
def C():
    def gcd(a,b):
        if a == 0:
            return b
        return gcd(b%a,a)
    n = I()
    a = LI()
    g = a[0]
    for i in range(1,n):
        g = gcd(g,a[i])
    print(g)
    return

#D
def D():
    n,m = LI()
    a = LI()
    f = [0,2,5,5,4,5,6,3,7,6]
    dp = [None for i in range(n+1)]
    dp[0] = []
    for j in a:
        for i in range(n+1):
            if i-f[j] >= 0 and dp[i-f[j]] != None:
                if dp[i] == None:
                    dp[i] = dp[i-f[j]]+[j]
                    dp[i].sort(reverse = True)
                elif len(dp[i]) < len(dp[i-f[j]])+1:
                    dp[i] = dp[i-f[j]]+[j]
                    dp[i].sort(reverse = True)
                elif len(dp[i]) == len(dp[i-f[j]])+1:
                    d = dp[i-f[j]]+[j]
                    d.sort(reverse = True)
                    if dp[i] < d:
                        dp[i] = d
    ans = 0
    k = pow(10,len(dp[n])-1)
    for i in range(len(dp[n])):
        ans += k*dp[n][i]
        k //= 10
    print(ans)
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
    D()
