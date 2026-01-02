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
    n,k = LI()
    a = LI()
    s = [0]
    for i in a:
        s.append((s[-1]+i-1)%k)
    ans = 0
    d = defaultdict(lambda : 0)
    for i in range(n+1):
        ans += d[s[i]]
        d[s[i]] += 1
        j = i-k+1
        if j >= 0:
            d[s[j]] -= 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
