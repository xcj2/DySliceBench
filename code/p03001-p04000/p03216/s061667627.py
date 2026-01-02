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
    s = input()
    q = I()
    K = LI()
    for k in K:
        ans = 0
        sa = 0
        sb = 0
        ns = 0
        for i in range(n):
            if i >= k:
                j = i-k
                if s[j] == "D":
                    sa -= 1
                    ns -= sb
                elif s[j] == "M":
                    sb -= 1
            if s[i] == "D":
                sa += 1
            elif s[i] == "M":
                sb += 1
                ns += sa
            elif s[i] == "C":
                ans += ns
        print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
