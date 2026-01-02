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
    n,x,y = LI()
    x -= 1
    y -= 1
    ans = [0]*n
    for i in range(n):
        k = abs(x-i)
        for j in range(i+1,n):
            d = min(j-i,k+abs(j-y)+1)
            ans[d] += 1
    for i in ans[1:]:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
