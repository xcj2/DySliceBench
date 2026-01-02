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
    v = [[] for i in range(n)]
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    bfs = [0]*n
    bfs[0] = 1
    q = deque([0])
    while q:
        x = q.popleft()
        if bfs[x] == 1:
            nb = 2
        elif bfs[x] == 2:
            nb = 1
        else:
            nb = 3
        for y in v[x]:
            if bfs[y]^nb:
                bfs[y] |= nb
                q.append(y)
    ans = 0
    f = [0]*3
    for b in bfs:
        if b == 1:
            ans += f[0]
            f[1] += 1
            f[2] += 1
        elif b == 2:
            ans += f[1]
            f[0] += 1
            f[2] += 1
        else:
            ans += f[2]
            f[0] += 1
            f[1] += 1
            f[2] += 1
    print(ans-m)
    return


#Solve
if __name__ == "__main__":
    solve()
