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
    a = LI()
    f = list(set(a))
    f.sort()
    s = [0]*len(f)
    ind = [0]*n
    for i in range(n):
        j = bisect.bisect_left(f,a[i])
        s[j] += 1
    ls = list(accumulate(s))
    rs = list(accumulate(s[::-1]))[::-1]
    ans = 0
    fact = [1]
    N = 10**5
    for i in range(1,N+1):
        fact.append(fact[-1]*i%mod)
    inv = [0]*(N+1)
    inv[N] = pow(fact[N],mod-2,mod)
    for i in range(N)[::-1]:
        inv[i] = inv[i+1]*(i+1)%mod
    comb = lambda x,y:fact[x]*inv[y]*inv[x-y]%mod
    for j in a:
        i = bisect.bisect_left(f,j)
        l = ls[i]-1
        r = rs[i]-1
        cl = comb(l,k-1) if l >= k-1 else 0
        cr = comb(r,k-1) if r >= k-1 else 0
        ans += f[i]*(cl-cr)
        ans %= mod
        ls[i] -= 1
        rs[i] -= 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
