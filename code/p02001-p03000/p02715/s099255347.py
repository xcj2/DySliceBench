#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from heapq import heappush, heappop, heapify

import itertools, bisect
import math, fractions
import sys, copy

def L(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline().rstrip())
def S(): return list(sys.stdin.readline().rstrip())
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007
INF = float("inf")

class Eratosthenes:
    # https://cp-algorithms.com/algebra/prime-sieve-linear.html
    def __init__(self, n):
        primes = []
        lp = [0] * (n + 1)

        for i in range(2, n + 1):
            if lp[i] == 0:
                primes.append(i)
                lp[i] = i

            for pj in primes:
                if pj > lp[i] or i * pj > n:
                    break
                lp[i * pj] = pj
        self.primes = primes
        self.lp = lp

    def is_prime(self, x):
        return self.lp[x] == x

    def factrization(self, x):
        ret = []
        while x > 1:
            ret.append(self.lp[x])
            x //= self.lp[x]
        return ret

def main():
    N, K = LI()

    era = Eratosthenes(K)
    count = [0] * (K + 1)

    for i in range(1, K + 1):
        count[i] = pow((K // i), N, MOD)

    for i in range(1, K + 1)[::-1]:
        divs = era.factrization(i)
        candedates = [l for l in set(reduce(lambda x, y:x * y, ll, 1) for r in range(1, len(divs) + 1) for ll in itertools.combinations(divs, r))]
        for v in candedates:
            count[i // v] -= count[i]

    ans = 0
    for i in range(1, K + 1):
        ans = (ans + i * count[i]) % MOD
    print(ans % MOD)

if __name__ == '__main__':
    main()