#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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

def solve():
    n = I()
    x = LI()
    fact = [1]
    for i in range(1,n):
        fact.append(fact[-1]*i%mod)
    S = [fact[n-1]*pow(i,mod-2,mod)%mod for i in range(1,n)]
    for i in range(n-2):
        S[i+1] += S[i]
        S[i+1] %= mod
    ans = 0
    for i in range(n-1):
        d = x[i+1]-x[i]
        ans += d*S[i]%mod
        ans %= mod
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
