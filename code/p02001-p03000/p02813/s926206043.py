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
    def sum(i,bit):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i&-i
        return res

    def index_permutations(p):
        res = 0
        bit = [0]*(n+1)
        for i in range(len(p)):
            res += (p[i]-sum(p[i],bit))*f[n-i-1]
            j = p[i]
            while j <= n:
                bit[j] += 1
                j += j&-j
        return res
    n = I()
    p = LI()
    q = LI()
    f = [1]
    for i in range(1,n+1):
        f.append(f[-1]*i)
    print(abs(index_permutations(p)-index_permutations(q)))
    return

#Solve
if __name__ == "__main__":
    solve()
