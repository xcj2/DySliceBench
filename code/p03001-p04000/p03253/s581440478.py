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
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    n,h,w = LI()
    x = LI()
    t = [0 for i in range(w*n+1)]
    for i in range(n):
        if not i%2:
            t[i*w+x[i]] += 1
            t[(i+1)*w+x[i]] -= 1
        else:
            t[i*w-x[i]] += 1
            t[(i+1)*w-x[i]] -= 1
    for i in range(w*n):
        t[i+1] += t[i]
    ans = 0
    for i in t[:-1]:
        if i == 0:
            ans += h
    print(ans)
    return

#B
def B():
    def dfs(d,x):
        for i in range(d):
            print(".",end = "")
        print(lis[x])
        for y in v[x]:
            dfs(d+1,y)

    n = I()
    v = [[] for i in range(n)]
    lis = [None for i in range(n)]
    for i in range(n):
        k = I()
        lis[i] = input()
        if k > 0:
            v[k-1].append(i)
    dfs(0,0)
    return

#C
def C():
    def dfs(d,k):
        if d == n:
            l.append(k)
        else:
            if sum(k[-2:]) == 0 and len(k) > 1:
                dfs(d+1,k+[1])
            elif d == n-1:
                dfs(d+1,k+[1])
            else:
                dfs(d+1,k+[0])
                dfs(d+1,k+[1])
    n = I()
    l = []
    dfs(0,[])
    print(len(l))
    return

#D
def D():
    def factorize(n):
        if n < 4:
            return {n:1}
        lis = {}
        i = 2
        m = n
        while i**2 <= m:
            if m%i == 0:
                lis[i] = 0
                while m%i == 0:
                    m //= i
                    lis[i] += 1
            i += 1
        if m != 1:
            lis[m] = 1
        return lis
    n,m = LI()
    if m == 1:
        print(1)
        quit()
    l = factorize(m)
    fact = [None for i in range(200001)]
    fact[0] = 1
    for i in range(200000):
        fact[i+1] = fact[i]*(i+1)
        if fact[i+1] >= mod:
            fact[i+1] %= mod
    inv = [None for i in range(200001)]
    inv[200000] = pow(fact[200000],mod-2,mod)
    for i in range(200000)[::-1]:
        inv[i] = inv[i+1]*(i+1)
        if inv[i] >= mod:
            inv[i] %= mod
    ans = 1
    for i in l.values():
        ans *= (fact[n+i-1]*inv[i]*inv[n-1])%mod
        if ans >= mod:
            ans %= mod
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

#I
def I_():
    return

#J
def J():
    return

#Solve
if __name__ == "__main__":
    D()
