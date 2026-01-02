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
    c = input()
    r = deque()
    for i in range(n)[::-1]:
        if c[i] == "R":
            r.append(i)
    if len(r) in (0, n):
        print(0)
        return
    ans = 0
    for i in range(n):
        if c[i] == "W":
            while r:
                j = r.popleft()
                if j > i:
                    break
            else:
                print(ans)
                return
            ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
