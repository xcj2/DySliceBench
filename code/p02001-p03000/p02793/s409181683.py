from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import factorial, ceil, floor, gamma, log
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
mod = 10 ** 9 + 7

def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass

def prime_decomposition(n):
    table = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            table += [i]
            n //= i
        if n == 1:
            break
    if n != 1:
        table += [a]
    return table

pr = primes(10 ** 3 + 1)
n = I()
A = LI()
D = defaultdict(int)
for a in A:
    for p in pr:
        if a < p:
            break
        cnt = 0
        while a % p == 0:
            cnt += 1
            a //= p
        if cnt > D[p]:
            D[p] = cnt
    if a > 1 and D[a] == 0:
        D[a] = 1

lcm = 1
for v in D:
    lcm = lcm * pow(v, D[v], mod) % mod

ans = 0
for a in A:
    ans = (ans + pow(a, mod-2, mod) * lcm % mod) % mod



print(ans)