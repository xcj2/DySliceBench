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
    n,k = LI()
    a = LI()
    dp = [0 for i in range(k+1)]
    f = [0 for i in range(k+1)]
    for i in range(k+1):
        if not f[i]:
            for j in a:
                if i-j >= 0:
                    dp[i] = 1-dp[i-j]
                    if dp[i] == 0:
                        break
            else:
                dp[i] = 1
    print(["First","Second"][dp[k]])
#B
def B():
    n = I()
    a = LI()
    ma = n*(n+1)//2
    su = sum(a)
    s = [1 for i in range(n+1)]
    for i in range(1,n):
        s[i+1] = s[i]+n-i+1
    d = [None for i in range(ma+1)]
    d[0] = 0
    k = 1
    for i in range(1,n+1):
        for j in range(n+1-i):
            d[k+j] = i
        k += n+1-i
    k = n%2
    dp = [su if (d[i]+k)%2 else -su for i in range(ma+1)]
    dp[0] = 0
    if k:
        for i in range(n):
            dp[i+1] = a[n-1-i]
    else:
        for i in range(n):
            dp[i+1] = -a[n-1-i]
    for i in range(1,ma):
        r = n-1-(i-s[d[i]])
        l = r+1-d[i]
        j = i+(n-d[i])
        j2 = j+1
        if (d[i]+k)%2:
            if r < n-1:
                if a[r+1]+dp[i] > dp[j]:
                    dp[j] = a[r+1]+dp[i]
            if l > 0:
                if a[l-1]+dp[i] > dp[j2]:
                    dp[j2] = a[l-1]+dp[i]
        else:
            if r < n-1:
                if -a[r+1]+dp[i] < dp[j]:
                    dp[j] = -a[r+1]+dp[i]
            if l > 0:
                if -a[l-1]+dp[i] < dp[j2]:
                    dp[j2] = -a[l-1]+dp[i]
    print(dp[ma])
    return

#C
def C():
    def comb(a,b):
        return fact[a]*inv[b]*inv[a-b]%mod

    n,k = LI()
    a = LI()
    """
    fact = [1]
    for i in range(n+k):
        fact.append(fact[-1]*(i+1)%mod)
    inv = [1]*(n+k+1)
    inv[n+k] = pow(fact[n+k],mod-2,mod)
    for i in range(n+k)[::-1]:
        inv[i] = inv[i+1]*(i+1)%mod
    f = [comb(i+n-1,n-1) for i in range(k+1)]
    for i in a:
        for j in range(k-i)[::-1]:
            f[j+i+1] -= f[j]
            f[j+i+1] %= mod
    print(f[k])
    """
    dp = [[0]*(k+1) for i in range(n+1)]
    for i in range(k+1):
        dp[0][i] = 1
    for i in range(n):
        ni = i+1
        ai = a[i]
        for j in range(k+1):
            if j >= ai+1:
                dp[ni][j] = (dp[i][j]-dp[i][j-ai-1])%mod
            else:
                dp[ni][j] = dp[i][j]
        if i < n-1:
            for j in range(k):
                dp[ni][j+1] += dp[ni][j]
                dp[ni][j+1] %= mod
    print(dp[n][k]%mod)
    return

#D
def D():
    n = I()
    a = LI()
    a.insert(0,0)
    for i in range(n):
        a[i+1] += a[i]
    dp = [[0]*(n+1) for i in range(n)]
    for le in range(1,n):
        for l in range(n-le):
            r = l+le+1
            res = float("inf")
            for i in range(l+1,r):
                m = dp[l][i]+dp[i][r]
                if m < res:
                    res = m
            res += a[r]-a[l]
            dp[l][r] = res
    print(dp[0][n])
    return

#E
def E():
    def bit_count(n):
        return bin(n).count("1")

    n = I()
    a = LIR(n)
    m = 1<<n
    dp = [0]*m
    dp[0] = 1
    a = [[j for j in range(n) if a[i][j]] for i in range(n)]
    for k in range(1,m):
        i = bit_count(k)-1
        for j in a[i]:
            bj = 1<<j
            if bj > k:
                break
            if not k&bj:
                continue
            nk = k^bj
            dp[k] += dp[nk]
            dp[k] %= mod
    print(dp[m-1])
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
    E()
