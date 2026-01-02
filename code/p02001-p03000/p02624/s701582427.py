from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd, sqrt
from operator import mul
from functools import reduce
from operator import mul
from pprint import pprint



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



def prime_decomposition(n):
    table = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            table += [i]
            n //= i
        if n == 1:
            break
    if n != 1:
        table += [n]
    return table

n = I()

ans  = 0
for i in range(1, n + 1):
    r = n - n % i
    cnt = n // i
    ans += (i + r) * cnt // 2




print(ans)
