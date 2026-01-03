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
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007



def comb(n, r):
    if r > n: return 0
    fact = 1
    for i in range(n-r+1, n+1):
        fact *= i


    divisor = 1
    for j in range(1, r+1):
        divisor *= j


    return fact // divisor




n, p = LI()
L = [i%2 for i in LI()]
ans = 0
odd_cnt = L.count(1)
even_cnt = L.count(0)
for k in range(p, odd_cnt+1, 2):
    ans += comb(odd_cnt, k) * 2 ** even_cnt



print(ans)