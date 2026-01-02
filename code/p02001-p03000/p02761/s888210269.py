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
    def check(i):
        i = str(i)
        for j in range(n):
            if d[j] >= 0:
                if int(i[j]) != d[j]:
                    return 0
        return 1
    n,m = LI()
    s = LIR(m)
    d = defaultdict(lambda : -1)
    for i,j in s:
        i -= 1
        if d[i] != -1 and d[i] != j:
            print(-1)
            return
        d[i] = j
    for i in range(10**(n-1) if n > 1 else 0, 10**n):
        if check(i):
            print(i)
            return
    print(-1)
    return

#Solve
if __name__ == "__main__":
    solve()
