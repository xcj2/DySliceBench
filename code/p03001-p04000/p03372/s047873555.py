from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
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



n, c = LI()
clock_pos = []
value = []
for pos, v in LIR(n):
    clock_pos += [pos]
    value += [v]


rounding_max = [0]
counter_rounding_max = [0]
return_max = [0]
counter_return_max = [0]
ret = 0
counter_ret = 0
for i in range(n):
    ret += value[i]
    counter_ret += value[-i - 1]
    rounding_max += [max(rounding_max[-1], ret - clock_pos[i])]
    counter_rounding_max += [max(counter_rounding_max[-1], counter_ret - (c - clock_pos[-i - 1]))]
    return_max += [max(return_max[-1], ret - clock_pos[i] * 2)]
    counter_return_max += [max(counter_return_max[-1], counter_ret - (c - clock_pos[-i - 1]) * 2)]



ans = max(rounding_max[-1], counter_rounding_max[-1])
for j in range(1, n + 1):
    ans = max(ans, return_max[j] + counter_rounding_max[n - j], counter_return_max[j] + rounding_max[n - j])


print(ans)