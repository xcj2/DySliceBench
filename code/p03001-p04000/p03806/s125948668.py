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
    n,A,B = LI()
    G = LIR(n)
    ma = sum([a for (a,_,_) in G])
    mb = sum([b for (_,b,_) in G])
    dp = [float("inf")]*((ma+1)*mb+1)
    dp[0] = 0
    for a,b,c in G:
        for sa in range(ma)[::-1]:
            na = sa+a
            if na > ma:
                continue
            for sb in range(mb)[::-1]:
                nb = sb+b
                if nb > mb:
                    continue
                nd = dp[sa*mb+sb]+c
                i = na*mb+nb
                if nd < dp[i]:
                    dp[i] = nd
    ans = float("inf")
    for i in range(1,ma+1):
        s = B*i
        if s%A:
            continue
        j = B*i//A
        if j > mb:
            continue
        k = i*mb+j
        if dp[k] < ans:
            ans = dp[k]
    if ans == float("inf"):
        print(-1)
        return
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
