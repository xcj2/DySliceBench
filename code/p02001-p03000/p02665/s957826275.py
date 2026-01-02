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
    n = I()
    a = LI()
    if n == 0:
        if a[0] == 1:
            print(1)
        else:
            print(-1)
        return
    if a[0] == 1:
        print(-1)
        return
    k = 1-a[0]
    M = [1]
    p = 1
    for i in range(n):
        if k <= 0:
            print(-1)
            return
        M.append(min(p,k) << 1)
        k = M[i+1] - a[i+1]
        p <<= 1
    if k < 0:
        print(-1)
        return
    s = a[-1]
    ans = s
    for i in range(n)[::-1]:
        s = min(M[i],s+a[i])
        ans += s
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
