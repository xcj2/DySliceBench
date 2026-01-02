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
    def check(y,x):
        res = 0
        c = s[x][y]
        for x in range(x,5):
            if s[x][y] != c:
                break
            res += 1
        if res < 3:
            return 0
        else:
            return res

    def update(y,x,d):
        for i in range(x,x+d):
            s[i][y] = 0

    def fall(s):
        q = [[] for i in range(5)]
        for x in range(5):
            for y in range(h):
                if s[x][y]:
                    q[x].append(s[x][y])
            for y in range(h-len(q[x])):
                q[x].append(0)
        return q

    while 1:
        h = I()
        if h == 0:
            break
        s = LIR(h)
        s = [[s[-1-y][x] for y in range(h)] for x in range(5)]
        ans = 0
        f = 1
        while f:
            f = 0
            for y in range(h):
                for x in range(3):
                    if s[x][y]:
                        d = check(y,x)
                        ans += s[x][y]*d
                        if d:
                            update(y,x,d)
                            f = 1
            if f:
                s = fall(s)
        print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()

