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
def S(): return list(sys.stdin.readline())[:-1]
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

M = 10000
l = [1]*(M+1)
prime = []
p = 2
while p <= M:
    while p <= M and not l[p]:
        p += 1
    j = p
    while j <= M:
        l[j] = 0
        j += p
    prime.append(p)
l = len(prime)
def solve(m,a,b):
    ans = [0,0,0]
    for i in range(l):
        p = prime[i]
        k = min(l,bisect.bisect_right(prime,p*b/a)+1,bisect.bisect_right(prime,m/p)+1)
        for j in range(max(0,k-3),k):
            q = prime[j]
            if p <= q:
                if a*q <= b*p:
                    s = p*q
                    if s <= m:
                        if ans[0] <= s:
                            ans = [s,p,q]
    print(*ans[1:])
    return

#Solve
if __name__ == "__main__":
    while 1:
        m,a,b = LI()
        if m == a == b == 0:
            break
        solve(m,a,b)

