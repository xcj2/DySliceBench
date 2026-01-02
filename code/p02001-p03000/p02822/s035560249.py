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
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    q = deque([0])
    d = [0]*n
    d[0] = 1
    pre = [None]*n
    while q:
        x = q.popleft()
        nd = d[x]+1
        for y in v[x]:
            if not d[y]:
                d[y] = nd
                pre[y] = x
                q.append(y)
    V = list(range(1,n))
    V.sort(key = lambda x:-d[x])
    size = [1]*n
    for i in V:
        size[pre[i]] += size[i]
    inv = pow(2,mod-2,mod)
    ans = (1-pow(inv,n,mod)-n*inv)%mod
    p = [pow(inv,i,mod) for i in range(n)]
    for i in range(1,n):
        a = size[i]
        b = n-a
        ans += (p[a]-1)*(p[b]-1)%mod
        ans %= mod
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
