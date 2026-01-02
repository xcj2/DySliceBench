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
    a,b,c = LI()
    if a == b and b == c:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    n = I()
    s = S()
    r = s.count("R")
    if r > n//2:
        print("Yes")
    else:
        print("No")
    return

#C
def C():
    n,q = LI()
    s = input()
    l = -1
    r = n
    t = [input().split() for i in range(q)]
    for i in range(q)[::-1]:
        a,b = t[i]
        if b == "R":
            if r > 0 and s[r-1] == a:
                r -= 1
            if l >= 0 and s[l] == a:
                l -= 1
        else:
            if l < n-1 and s[l+1] == a:
                l += 1
            if r < n and s[r] == a:
                r += 1
    ans = max(0,r-l-1)
    print(ans)
    return

#D
def D():
    n,x = LI()
    s = LI()
    m = min(s)
    k = [s[i] for i in range(n)]
    dfs(0,x,k,m,n)
    print(ans%mod)
    return

#E
def E():
    def com(a,b):
        return fact[a]*inv[b]*inv[a-b]%mod
    fact = [1 for i in range(100001)]
    for i in range(100000):
        fact[i+1] = fact[i]*(i+1)%mod
    inv = [1 for i in range(100001)]
    inv[100000] = pow(fact[100000],mod-2,mod)
    for i in range(100000)[::-1]:
        inv[i] = inv[i+1]*(i+1)%mod
    b,w = LI()
    n = b+w
    po = [1 for i in range(100001)]
    for i in range(100000):
        po[i+1] = po[i]*2%mod
    inp = [1 for i in range(100001)]
    inp[100000] = pow(po[100000],mod-2,mod)
    for i in range(100000)[::-1]:
        inp[i] = inp[i+1]*2%mod
    for i in range(1,n+1):
        ans = 0
        if i < n:
            if i < b:
                for k in range(1,i+1):
                    ans += inp[i]*com(i-1,k-1)%mod
                    ans %= mod
            else:
                for k in range(1,b):
                    ans += inp[i]*com(i-1,k-1)%mod
                    ans %= mod
                for k in range(b,i+1):
                    ans += inp[i-1]*com(i-1,k-1)%mod
                    ans %= mod
        else:
            for k in range(n-w+1,b):
                ans += inp[i]*com(i-1,k-1)%mod
                ans %= mod
            for k in range(b,i):
                ans += inp[i-1]*com(i-1,k-1)%mod
                ans %= mod
            ans *= inp[i-2]*com(i-1,k-1)%mod
            ans %= mod
        print(ans)
        print
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
