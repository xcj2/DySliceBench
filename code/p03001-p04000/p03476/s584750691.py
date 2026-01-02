from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, atan2, degrees
from operator import mul
from functools import reduce
sys.setrecursionlimit(10**8)

INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
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



n = 10 ** 5
prime_set = primes(n)
q = I()
C = [0] * (n + 1)
for i in range(n + 1):
    if i % 2 and i in prime_set and (i + 1) // 2 in prime_set:
        C[i] = 1


acc = list(accumulate(C))
for i in range(q):
    l, r = LI()
    print(acc[r] - acc[l - 1])
