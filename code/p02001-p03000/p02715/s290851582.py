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
    n,k = LI()
    if k == 2:
        print((pow(2,n,mod)+1)%mod)
    elif k == 3:
        print((pow(3,n,mod)+3)%mod)
    elif k == 4:
        print((pow(4,n,mod)+pow(2,n,mod)+4)%mod)
    elif k == 5:
        print((pow(5,n,mod)+pow(2,n,mod)+8)%mod)
    else:
        f = [-1]*(k+1)
        p = 2
        while p <= k:
            x = 2*p
            while x <= k:
                f[x] -= f[p]
                x += p
            p += 1
        ans = 0
        p = [1]
        for i in range(1,k+1):
            p.append(pow(k//i,n,mod))
        for i in range(1,k+1):
            res = p[i]
            x = 2*i
            j = 2
            while x <= k:
                res += p[x]*f[j]
                x += i
                j += 1
            ans += i*res
            ans %= mod
        print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
