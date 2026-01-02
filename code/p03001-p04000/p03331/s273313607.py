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
    def digitsum(n):
        res = 0
        while n:
            res += n%10
            n //= 10
        return res
    n = I()
    ans = float("inf")
    for a in range(1,(n>>1)+1):
        b = n-a
        m = digitsum(a)+digitsum(b)
        if m < ans:
            ans = m
    print(ans)
    return

#B
def B():
    def comb(a,b):
        return fact[a]*inv_fact[b]*inv_fact[a-b]%mod
    mod = 998244353
    n,a,b,k = LI()
    fact = [1]*(n+1)
    for i in range(1,n+1):
        fact[i] = fact[i-1]*i%mod
    inv_fact = [None]*(n+1)
    inv_fact[n] = pow(fact[n],mod-2,mod)
    for i in range(n)[::-1]:
        inv_fact[i] = inv_fact[i+1]*(i+1)%mod

    ans = 0
    for x in range(n+1):
        if (k-a*x)%b == 0 and k >= a*x and k-a*x <= n*b:
            y = (k-a*x)//b
            ans += comb(n,x)*comb(n,y)%mod
        ans %= mod
    print(ans)

#C
def C():
    n = I()
    d = LIR(n)
    x = [None for i in range(n)]
    for i in range(n):
        if d[i][0]*d[i][1] <= 0:
            x[i] = 0
        else:
            if d[i][1] < 0:
                x[i] = d[i][1]
            else:
                x[i] = d[i][0]
    x.sort(key = lambda x:x)
    l = 0
    r = n-1
    ans = abs(x[l])
    k = 1
    while r-l > 0:
        ans += x[r]-x[l]
        if k:
            k = 0
            l += 1
        else:
            k = 1
            r -= 1
    ans += abs(x[r])
    l = 0
    r = n-1
    ans2 = abs(x[r-1])
    k = 0
    while r-l > 0:
        ans2 += x[r]-x[l]
        if k:
            k = 0
            l += 1
        else:
            k = 1
            r -= 1
    ans2 += abs(x[r])
    print(max(ans,ans2))
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
    A()
