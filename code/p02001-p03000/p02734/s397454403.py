#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]


mod = 998244353
inf = 1e10

#solve
def solve():
    n, s = LI()
    a = LI()
    dp1 = [0] * (3000 + 1)
    dp2 = [0] * (3000 + 1)
    ans = 0

    for i in range(n):
        for j in range(s+1):
            dp2[j] = dp1[j]
        
        for j in range(a[i], s + 1):
            dp2[j] += dp1[j - a[i]]
            dp2[j] %= mod
        dp2[a[i]] += i + 1 
        ans += dp2[s]
        ans %= mod
        dp1 = dp2[::1]
        # print(dp2)
    print(ans)
            
    return


#main
if __name__ == '__main__':
    solve()
