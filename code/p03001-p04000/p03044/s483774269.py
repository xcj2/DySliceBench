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
    v = [[] for i in range(n)]
    for i in range(n-1):
        a,b,c = LI()
        a -= 1
        b -= 1
        v[a].append((b,c))
        v[b].append((a,c))
    bfs = [-1]*n
    q = deque([0])
    bfs[0] = 0
    ans = [0]*n
    while q:
        x = q.popleft()
        for y,c in v[x]:
            nd = bfs[x]+c
            if bfs[y] < 0:
                bfs[y] = nd
                ans[y] = nd&1
                q.append(y)
    for i in ans:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
