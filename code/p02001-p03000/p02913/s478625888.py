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
    s = input()
    if s == "Sunny":
        print("Cloudy")
    elif s == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")
    return

#B
def B():
    s = S()
    for i in range(len(s)):
        if i%2:
            if s[i] not in ["L","U","D"]:
                print("No")
                return
        else:
            if s[i] not in ["R","U","D"]:
                print("No")
                return
    print("Yes")
    return

#C
def C():
    n,k,q = LI()
    a = IR(q)
    f = [k-q]*(n)
    for i in range(q):
        ai = a[i]-1
        f[ai] += 1
    for i in f:
        if i <= 0:
            print("No")
        else:
            print("Yes")
    return

#D
def D():
    n,m = LI()
    a = LI()
    q = []
    for i in range(n):
        heappush(q,-a[i])
    for i in range(m):
        x = heappop(q)
        x *= -1
        x >>= 1
        heappush(q,-x)
    print(-sum(q))
    return

#E
def E():
    n = I()
    s = S()
    l = 0
    r = n
    M = 10**64+1
    b = 26
    alp = list("abcdefghijklmnopqrstuvwxyz")
    f = {}
    for i in alp:
        f[i] = ord(i)-ord("a")
    pb = [pow(b,i,M) for i in range(n+1)]
    while r-l > 1:
        m = (l+r)>>1
        d = defaultdict(lambda : float("inf"))
        hash = 0
        for i in s[:m]:
            hash *= b
            hash += f[i]
            hash %= M
        d[hash] = 0
        t = pb[m]
        for i in range(n-m):
            si = s[i]
            hash *= b
            hash -= t*f[si]
            hash += f[s[i+m]]
            hash %= M
            if d[hash]+m <= i+1:
                l = m
                break
            if i+1 < d[hash]:
                d[hash] = i+1
        else:
            r = m
    print(l)
    return

#F
def F():

    return

#Solve
if __name__ == "__main__":
    E()
