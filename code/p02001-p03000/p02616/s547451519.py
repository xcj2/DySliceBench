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
    n,k = LI()
    a = LI()
    a.sort(key = lambda x:-abs(x))
    p = 0
    m = 0
    for i in a:
        if i >= 0:
            p += 1
        else:
            m += 1
    f = 1
    for x in range(min(p,k)+1):
        y = k-x
        if y < 0 or y > m:
            continue
        if not y&1:
            f = 0
            break
    if f:
        a.sort(key = lambda x:abs(x))
        ans = 1
        for i in a[:k]:
            ans *= i
            ans %= mod
        print(ans)
        return
    minus = []
    s = 1
    s2 = 1
    k1 = 0
    k2 = 0
    ans = 1
    if k&1:
        m = max(a)
        for i in range(n):
            if a[i] == m:
                break
        a = a[:i]+a[i+1:]
        ans *= m
        k -= 1
    for i in a:
        if i < 0:
            k1 ^= 1
            s *= -i
            if not k1:
                minus.append(s)
                s = 1
        else:
            k2 ^= 1
            s2 *= i
            if not k2:
                minus.append(s2)
                s2 = 1
    x = k>>1
    minus.sort(reverse = True)
    for m in minus[:x]:
        ans *= m
        ans %= mod
    print(ans%mod)
    return

#Solve
if __name__ == "__main__":
    solve()
