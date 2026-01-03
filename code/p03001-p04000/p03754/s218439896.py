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
    s = [0]*n
    e = [0]*n
    e[0] = 1
    while q:
        x = q.pop()
        for y in v[x]:
            if not e[y]:
                s[x] += 1
                e[y] = 1
                q.append(y)
                q2.append((y,x))

    while q2:
        y,x = q2.pop()
        e[x] += e[y]/s[x]
    ans = [None]*n
    ans[0] = e[0]
    q.append((0,s[0],e[0]))
    while q:
        x,sx,ex = q.pop()
        nsx = sx-1
        for y in v[x]:
            if ans[y] is None:
                sy,ey = s[y],e[y]
                nex = ((ex-1)*sx-ey)/nsx+1 if nsx else 1
                nsy = sy+1
                ans[y] = ney = ((ey-1)*sy+nex)/nsy+1
                q.append((y,nsy,ney))

    for i in ans:
        print(i-1)
    return

#Solve
if __name__ == "__main__":
    solve()
