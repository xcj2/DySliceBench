from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007



q = I()


def sieve(r):
    not_prime = [0] * r
    not_prime[0] = 1
    not_prime[1] = 1
    for i in range(2, r):
        if not_prime[i] == 0:
            for j in range(i*2, r, i):
                not_prime[j] = 1
    return [k for k in range(r) if not not_prime[k]]



primes = sieve(100)
n = len(primes)
multiple_cnt = [0] * n
for m in range(len(primes)):
    ret = q
    p = primes[m]
    while ret:
        ret //= p
        multiple_cnt[m] += ret


multiple_cnt.sort()
ans = 0
ans += (n - bisect_left(multiple_cnt, 74))
ans += (n - bisect_left(multiple_cnt, 24)) * (n - bisect_left(multiple_cnt, 2) - 1)
ans += (n - bisect_left(multiple_cnt, 14)) * (n - bisect_left(multiple_cnt, 4) - 1)
ans += (n - bisect_left(multiple_cnt, 4)) * (n - bisect_left(multiple_cnt, 4) - 1) // 2 * (n - bisect_left(multiple_cnt, 2) - 2)


print(ans)