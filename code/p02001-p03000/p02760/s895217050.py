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
    a = LIR(3)
    n = I()
    b = IR(n)
    f = defaultdict(lambda : 0)
    for i in b:
        f[i] = 1
    for i in range(3):
        m = 0
        for j in range(3):
            m += f[a[i][j]]
        if m == 3:
            print("Yes")
            return
        m = 0
        for j in range(3):
            m += f[a[j][i]]
        if m == 3:
            print("Yes")
            return
    m = 0
    for j in range(3):
        m += f[a[j][j]]
    if m == 3:
        print("Yes")
        return
    m = 0
    for j in range(3):
        m += f[a[-1-j][j]]
    if m == 3:
        print("Yes")
        return
    print("No")
    return

#Solve
if __name__ == "__main__":
    solve()
