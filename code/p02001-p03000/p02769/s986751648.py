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
mod = 1000000007
inf = float('INF')
fact = [i for i in range(4 * 10 ** 5 + 1)]
fact[0] = 1
for i in range(4 * 10 ** 5):
    fact[i + 1] *= fact[i]
    fact[i + 1] %= mod

def combination_mod(n, k, mod):
    """ power_funcを用いて(nCk) mod p を求める """
    """ nCk = n!/((n-k)!k!)を使用 """
    if n < 0 or k < 0 or n < k:
        return 0
    if n == 0 or k == 0:
        return 1
    a = fact[n] % mod
    b = fact[k] % mod
    c = fact[n - k] % mod
    return (a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod)) % mod

#solve
def solve():
    n, k = LI()

    if n <= k:
        print(combination_mod(2 * n - 1, n, mod))
    else:
        if k == 1:
            print(n * (n - 1))
        else:
            ans = 1
            for i in range(1, k + 1):
                ans += combination_mod(n - 1, n - i - 1, mod) * combination_mod(n, i, mod)
                ans %= mod
                # print(ans)
            print(ans)

    return


#main
if __name__ == '__main__':
    solve()
