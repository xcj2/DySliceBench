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
    n = I()
    v = [[] for i in range(n)]
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    q = [0]
    q2 = []
    g = [0]*n
    bfs = [1]*n
    bfs[0] = 0
    d = [0]*n
    while q:
        x = q.pop()
        for y in v[x]:
            if bfs[y]:
                bfs[y] = 0
                d[x] += 1
                q.append(y)
                q2.append((x,y))
    while q2:
        x,y = q2.pop()
        g[x] ^= g[y]+1
    ans = g[0]
    if ans:
        print("Alice")
    else:
        print("Bob")
    return

#Solve
if __name__ == "__main__":
    solve()
