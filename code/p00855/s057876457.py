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
M = 1500000
l = [1]*(M+1)
p = 2
prime = []
while p <= M:
    while p <= M and not l[p]:
        p += 1
    j = p
    while j <= M:
        l[j] = 0
        j += p
    prime.append(p)
    
def solve(k):
    i = bisect.bisect_left(prime,k)
    if prime[i] == k:
        print(0)
    else:
        print(prime[i] - prime[i-1])
    return

#Solve
if __name__ == "__main__":
    while 1:
        k = I()
        if k == 0:
            break
        solve(k)

