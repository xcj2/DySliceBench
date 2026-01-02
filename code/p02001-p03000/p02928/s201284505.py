from collections import defaultdict
from heapq import heappush, heappop
import math
import bisect
import random

def LI(): return list(map(int, input().split()))
def I(): return int(input())
def LIM(): return list(map(lambda x:int(x) - 1, input().split()))
def LS(): return input().split()
def S(): return input()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007


n, k = LI()
a_list = LI()


rev_tuple = []
for i in range(len(a_list)):
    num = a_list[i]
    a = len([j for j in a_list[i:] if j < num]) % mod
    b = len([j for j in a_list if j < num]) % mod
    rev_tuple += [(a, b)]



ans = 0

for a, b in rev_tuple:
    ans += b * k * (k - 1) // 2 % mod
    ans %= mod
    ans += a * k % mod
    ans %= mod





print(ans % mod)