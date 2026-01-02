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
factorial = [i for i in range(10 ** 5 + 1)]
for i in range(2, 10 ** 5 + 1):
    factorial[i] *= factorial[i - 1]
    factorial[i] %= mod

def combination_mod(n, k, mod):
    """ power_funcを用いて(nCk) mod p を求める """ 
    """ nCk = n!/((n-k)!k!)を使用 """

    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    if n == k: return 1
    a = factorial[n] % mod
    b = factorial[k] % mod
    c = factorial[n - k] % mod
    return (a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod)) % mod

#solve
def solve():
    n, k = LI()
    a = LI()
    a.sort()
    d = defaultdict(int)
    for i, ai in enumerate(sorted(set(a))):
        d[ai] = i
    cont = [0] * n
    for ai in a:
        cont[d[ai]] += 1
    mina = [0] + list(itertools.accumulate(cont))
    ans = 0
    for b, key in sorted(d.items()):
        mina_ = mina[key]
        count = n - mina_

        if count < k:
            continue
        else:
            # print(combination_mod(count, k, mod),combination_mod(count-cont[key], k, mod),count-cont[key])
            ans -= b*(combination_mod(count, k, mod)-combination_mod(count-cont[key], k, mod))
            ans %= mod

    for b, key in sorted(d.items()):
        mina_ = mina[key]
        count = cont[key] + mina_
        if count < k:
            continue
        else:
            ans += b*(combination_mod(count, k, mod)-combination_mod(count-cont[key], k, mod))
            ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
