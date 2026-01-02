#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
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
    def hadamard(n):
        if mem[n] != None:
            return mem[n]
        h = hadamard(n-1)
        res = [[j for j in i] for i in h]
        res_ = [[j for j in i] for i in h]
        for i in range(len(res)):
            res[i] += [j for j in h[i]]
            res_[i] += [j^1 for j in h[i]]
        res += res_
        mem[n] = res
        return res

    n,m = LI()
    f = 0
    if m < n:
        n,m = m,n
        f = 1
    h,w = 1<<n, 1<<m
    mem = defaultdict(lambda : None)
    mem[0] = [[0]]
    s = hadamard(m)[:h]
    if f:
        s = [[s[j][i] for j in range(h)] for i in range(w)]
        h,w = w,h
    for x in range(w):
        for y in range(h-1)[::-1]:
            s[y+1][x] ^= s[y][x]
    for y in range(h):
        for x in range(w-1)[::-1]:
            s[y][x+1] ^= s[y][x]
    ans = [i[1:] for i in s[1:]]
    for i in ans:
        print(*i,sep="")
    return

#Solve
if __name__ == "__main__":
    solve()
