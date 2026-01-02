#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
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
    def li(i):
        if i == 0:
            return [0,1]
        if i < 9:
            return [i-1,i,i+1]
        else:
            return [8,9]

    f = [(i,i) for i in range(1,10)]
    s = 10
    while len(f) < 10**5:
        nf = [(i*10+k,k) for (i,j) in f[-s:] for k in li(j)]
        f += nf
        s = len(nf)
    k = I()
    print(f[k-1][0])
    return

#Solve
if __name__ == "__main__":
    solve()
