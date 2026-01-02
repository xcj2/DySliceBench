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
    n,q = LI()
    v = [[] for i in range(n)]
    for _ in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    f = [0]*n
    for _ in range(q):
        p,x = LI()
        p -= 1
        f[p] += x
    d = [0]*n
    d[0] = 1
    q = deque([0])
    while q:
        x = q.popleft()
        fx = f[x]
        for y in v[x]:
            if not d[y]:
                d[y] = 1
                f[y] += fx
                q.append(y)
    print(*f)
    return

#Solve
if __name__ == "__main__":
    solve()
