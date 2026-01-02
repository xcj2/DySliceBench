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
    def comb(n,k):
        if n < k:
            return 0
        return f[n]*inv[k]*inv[n-k]%mod
    n,k = LI()
    a = LI()
    a.sort()
    f = [1]
    N = 10**6
    for i in range(1,N+1):
        f.append(f[-1]*i%mod)
    inv = [None]*(N+1)
    inv[N] = pow(f[N],mod-2,mod)
    for i in range(1,N+1)[::-1]:
        inv[i-1] = inv[i]*i%mod
    ans = 0
    d = defaultdict(lambda : 1)
    for i in a:
        l = bisect.bisect_right(a,i)-d[i]
        r = n-l-1
        d[i] += 1
        ans += i*(comb(l,k-1)-comb(r,k-1))%mod
        ans %= mod
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
