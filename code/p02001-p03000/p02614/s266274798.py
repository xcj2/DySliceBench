#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
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
    h,w,K = LI()
    c = [list(input()) for i in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == "#":
                c[i][j] = 1
            else:
                c[i][j] = 0
    n = h+w
    ans = 0
    for b in range(1<<n):
        nc = [[i for i in j] for j in c]
        for i in range(n):
            if (b>>i)&1:
                if i < h:
                    for k in range(w):
                        nc[i][k] = 0
                else:
                    j = i-h
                    for k in range(h):
                        nc[k][j] = 0
        s = sum([sum(i) for i in nc])
        if s == K:
            ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
