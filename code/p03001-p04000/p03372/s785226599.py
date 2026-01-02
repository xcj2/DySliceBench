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


n, c = LI()
clock_pos = []
value = []
for i, j in LIR(n):
    clock_pos += [i]
    value += [j]




arr = [0]
counter_arr = [0]
round_arr = [0]
round_counter_arr = [0]
ret = 0
counter_ret = 0
for i in range(n):
    ret += value[i]
    counter_ret += value[-i - 1]
    arr.append(max(arr[i], ret - clock_pos[i]))
    round_arr.append(ret - clock_pos[i] * 2)
    counter_arr.append(max(counter_arr[i], counter_ret - (c - clock_pos[-i - 1])))
    round_counter_arr.append(counter_ret - (c - clock_pos[-i - 1]) * 2)



ans = max(arr[-1], counter_arr[-1])
for j in range(n):
    ans = max(ans, round_arr[j] + counter_arr[n - j], round_counter_arr[j] + arr[n - j])


print(ans)
