#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
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
    def is_p(n):
        if n < 4:
            return 1
        i = 2
        while i*i <= n:
            if n%i == 0:
                return 0
            i += 1
        return 1

    def f(n):
        res = set([n])
        i = 2
        while i*i <= n:
            if n%i == 0:
                m = n//i
                res.add(i)
                res.add(m)
            i += 1
        res = list(res)
        res.sort()
        return res

    n = I()
    if n == 1:
        print(0)
        return
    if is_p(n):
        print(1)
        return
    f = f(n)
    m = len(f)
    k = [0]*m
    for i in range(m):
        fi = f[i]
        if is_p(fi):
            for j in range(i+1,m):
                if f[j]%fi == 0:
                    k[j] += 1
    lis = deque([f[i] for i in range(m) if k[i] <= 1])
    ans = 0
    while lis:
        x = lis.popleft()
        if n%x == 0:
            n //= x
            ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
