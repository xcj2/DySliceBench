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
    n,m = LI()
    s = LIR(m)
    p = LI()
    ans = 0
    for i in range(m):
        s[i] = sum([1<<(j-1) for j in s[i][1:]])
    for b in range(1<<n):
        for i in range(m):
            if bin(s[i]&b).count("1")&1 != p[i]:
                break
        else:ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
