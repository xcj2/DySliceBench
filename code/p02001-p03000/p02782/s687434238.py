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
inf = 1e10

# solve
# 解説AC
# f(r + 1, c) = f(r, 0) + f(r, 1) + ... + f(r, c)
# 図はこう
# .....147
# .....258
# .....369
# .....ACE
# .....BDF
# 4の通りはf(1)+f(2)+f(3)+f(A)+(B)
# てことはf(1)+f(2)+f(3) = f(4) - f(A) - f(B)
# さらにf(A)+f(B)=f(C)　なんで
# f(1)+f(2)+f(3) = f(4)-f(C)
# これを繰り返すだけ
# easy
def solve():
    def cmb(n, k):
        return fact[n] * invfact[k] * invfact[n-k] % mod
    maxn = int(3e6 + 10)
    r1, c1, r2, c2 = LI()
    ans = 0
    fact = [i for i in range(maxn)]
    fact[0] = 1
    invfact = [i+1 for i in range(maxn)]
    invfact[0] = 1
    for i in range(1, maxn-1):
        fact[i + 1] *= fact[i]
        fact[i + 1] %= mod
    invfact[-1] = pow(fact[-1], mod - 2, mod)
    invr1 = pow(r1, mod - 2, mod)
    for i in range(maxn - 2, -1, -1):
        invfact[i] *= invfact[i + 1]
        invfact[i] %= mod
    acc = list(map(lambda x: x % mod, itertools.accumulate(fact)))
    for c in range(c1, c2 + 1):
        ans += cmb(c + r2 + 1, c + 1) - cmb(c + r1 , c + 1)
        ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
