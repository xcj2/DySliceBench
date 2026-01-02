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
    n = I()
    v = [[] for i in range(n)]
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    d = [-1]*n
    d[0] = 0
    q = deque([0])
    while q:
        x = q.popleft()
        nd = d[x]^1
        for y in v[x]:
            if d[y] < 0:
                d[y] = nd
                q.append(y)
    n1 = sum(d)
    n0 = len(d)-n1
    if n1 > n0:
        for i in range(n):
            d[i] ^= 1
        n0,n1 = n1,n0
    p = [(n+2)//3, (n+1)//3, n//3]
    k = [1,2,3]
    ans = [0]*n
    if n1 >= p[1]:
        for i in range(n):
            di = d[i]
            if not p[di]:
                di = 2
            ans[i] = k[di]
            k[di] += 3
            p[di] -= 1
    else:
        for i in range(n):
            di = d[i]
            if di == 1:
                di = 2
            while not p[di]:
                di += 1
            ans[i] = k[di]
            k[di] += 3
            p[di] -= 1
    print(*ans)
    return

#Solve
if __name__ == "__main__":
    solve()
