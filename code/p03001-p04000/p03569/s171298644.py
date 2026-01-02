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
    s = input()
    t = []
    for i,si in enumerate(s):
        if si != "x":
            t.append((i,si))
    q = [i[1] for i in t]
    if q != q[::-1]:
        print(-1)
        return
    n = len(t)
    if not n:
        print(0)
        return
    m = n >> 1
    l = t[m-(1-(n&1))][0]
    r = t[m][0]
    ans = 0
    while l >= 0 or r < len(s):
        if l < 0:
            r += 1
            ans += 1
        elif r >= len(s):
            l -= 1
            ans += 1
        elif s[l] == s[r]:
            l -= 1
            r += 1
        elif s[l] == "x":
            l -= 1
            ans += 1
        else:
            r += 1
            ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
