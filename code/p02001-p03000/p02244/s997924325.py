#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
    k = I()
    n = 8
    a = [-1]*n
    for i in range(k):
        y,x = LI()
        a[y] = x
    for p in permutations(range(n)):
        f = 0
        for i in range(n):
            if a[i] >= 0 and a[i] != p[i]:
                f = 1
                break
            for j in range(i):
                if abs(i-j) == abs(p[i]-p[j]):
                    f = 1
                    break
            if f:
                break
        if f:
            continue
        ans = [["Q" if p[i] == j else "." for j in range(n)] for i in range(n)]
        for i in ans:
            print(*i,sep="")
        return
    return

#Solve
if __name__ == "__main__":
    solve()

