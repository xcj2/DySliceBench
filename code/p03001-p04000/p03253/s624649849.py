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
sys.setrecursionlimit(1000000)

#A
def A():
    return

#B
def B():
    return

#C
def C():
    s = S()
    t = S()
    n = len(s)
    d = defaultdict(list)
    for i in range(n):
        d[s[i]].append(t[i])
    d2 = defaultdict(list)
    for i in range(n):
        d2[t[i]].append(s[i])
    for i in d.keys():
        k = d[i]
        k = list(set(d[i]))
        if len(k) > 1:
            print("No")
            quit()
    for i in d2.keys():
        k = d2[i]
        k = list(set(d2[i]))
        if len(k) > 1:
            print("No")
            quit()
    print("Yes")
#D
def D():
    n,m = LI()
    if m == 1:
        print(1)
        quit()
    d = defaultdict(int)
    i = 2
    a = m
    while i**2 <= m:
        if not a%i:
            while not a%i:
                a//=i
                d[i] += 1
        i += 1
    if a != 1:
        d[a] += 1
    fact = [1 for i in range(n+31)]
    for i in range(n+30):
        fact[i+1] = fact[i]*(i+1)%mod
    inv_fact = [None for i in range(n+31)]
    inv_fact[n+30] = pow(fact[n+30],mod-2,mod)
    for i in range(n+30)[::-1]:
        inv_fact[i] = inv_fact[i+1]*(i+1)%mod
    ans = 1
    for i in d.values():
        ans *= fact[i+n-1]*inv_fact[i]*inv_fact[n-1]%mod
        ans %= mod
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
    D()
