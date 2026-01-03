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



n, limit = LI()
weight = []
value = []
for w, v in LIR(n):
    weight += [w]
    value += [v]


w1 = min(weight)
w2, w3, w4 = w1 + 1, w1 + 2, w1 + 3
w1_list = [0] + list(accumulate(sorted([value[i] for i in range(n) if weight[i] == w1], reverse=True)))
w2_list = [0] + list(accumulate(sorted([value[i] for i in range(n) if weight[i] == w2], reverse=True)))
w3_list = [0] + list(accumulate(sorted([value[i] for i in range(n) if weight[i] == w3], reverse=True)))
w4_list = [0] + list(accumulate(sorted([value[i] for i in range(n) if weight[i] == w4], reverse=True)))


ans = 0
for i, j, k, l in product(range(len(w1_list)), range(len(w2_list)), range(len(w3_list)), range(len(w4_list) )):
    if i * w1 + j * w2 + k * w3 + l * w4 > limit:
        continue
    ans = max(ans, w1_list[i] + w2_list[j] + w3_list[k] + w4_list[l])



print(ans)