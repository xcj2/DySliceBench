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
inf = float('INF')

#A
def A():
    n = II()
    n -= 1
    print(n // 2)
    return

#B
def combination_mod(n, k, mod=mod):
    """ power_funcを用いて(nCk) mod p を求める """ 
    """ nCk = n!/((n-k)!k!)を使用 """

    from math import factorial
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    a = factorial(n) % mod
    b = factorial(k) % mod
    c = factorial(n - k) % mod
    return (a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod)) % mod
    

def B():
    n = II()
    d = LI()
    dic = defaultdict(int)
    if d[0] != 0 or 0 in d[1:]:
        print(0)
        return
    for di in d[1:]:
        dic[di] += 1
    ans = 1
    di = list(dic.items())
    di.sort()
    be = 1
    for _, b in di:
        ans *= pow(be, b, mod)
        be = b
    print(ans)
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    A()
