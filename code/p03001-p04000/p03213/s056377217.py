from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


def primes(n):
    is_prime = [1] * (n + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = 0
    return {i for i in range(n + 1) if is_prime[i]}


n = I()
prime_set = primes(n)
prime_cnt = Counter()
for p in prime_set:
    pi = p
    while pi < n:
        prime_cnt[p] += n // pi
        pi *= p


prime_cnt = [v for k, v in prime_cnt.most_common()][::-1]
m = len(prime_cnt)
print(m - bisect_left(prime_cnt, 74) + (m - bisect_left(prime_cnt, 24)) * (m - bisect_left(prime_cnt, 2) - 1)
    + (m - bisect_left(prime_cnt, 14)) * (m - bisect_left(prime_cnt, 4) - 1)
    + (m - bisect_left(prime_cnt, 4)) * ((m - bisect_left(prime_cnt, 4)) - 1) // 2 * ((m - bisect_left(prime_cnt, 2)) - 2))