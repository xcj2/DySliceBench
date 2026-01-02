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
    a,b,t = LI()
    k = t//a
    print(k*b)
    return

#B
def B():
    n = I()
    v = LI()
    c = LI()
    ans = 0
    for i in range(n):
        if v[i] > c[i]:
            ans += (v[i]-c[i])
    print(ans)
    return

#C
def C():
    def gcd(a,b):
        if a == 0:
            return b
        return gcd(b%a, a)
    n = I()
    a = LI()
    ans = 1
    for i in range(n):
        b = a[:i]+a[i+1:]
        g = b[0]
        for j in range(a):
            print()
    return

#D
def D():
    n = I()
    a = LI()
    k = 0
    for i in a:
        if i < 0:
            k += 1
    ans = 0
    m = float("inf")
    for i in a:
        ans += abs(i)
        m = min(m,abs(i))
    if k%2:
        ans -= 2*m
    print(ans)
    return


#Solve
if __name__ == "__main__":
    D()
