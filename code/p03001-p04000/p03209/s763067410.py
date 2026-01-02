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
    n,x = LI()
    l = [4*2**i-3 for i in range(n+1)]
    s = [2*2**i-1 for i in range(n+1)]
    ans = 0
    while x:
        if x == l[n]:
            ans += s[n]
            break
        if x <= l[n-1]+1:
            n -= 1
            x -= 1
        elif x < l[n]:
            ans += 1+s[n-1]
            x -= 2+l[n-1]
            n -= 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
