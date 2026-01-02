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




counter_clock_pos = [0] + [c - i for i in clock_pos][::-1]
clock_pos = [0] + clock_pos
clock_cumsum = list(accumulate([0] + value))
counter_clock_cumsum = [0] + list(accumulate(value[::-1]))
# counterではどこまで行くべきか
counter_limit = [0] * (n + 1)
last_max_index = 0
ret = 0
for k in range(n + 1):
    remain = counter_clock_cumsum[k] - counter_clock_pos[k]
    if remain > ret:
        ret = remain
        last_max_index = k
    counter_limit[k] = last_max_index


ans = 0
for i in range(n + 1):
# 時計まわりでとった数がi
    ans = max(ans, clock_cumsum[i] - clock_pos[i] * 2 + counter_clock_cumsum[
        counter_limit[n - i]] - counter_clock_pos[counter_limit[n - i]])


limit = [0] * (n + 1)
last_max_index = 0
ret = 0
for k in range(n + 1):
    remain = clock_cumsum[k] - clock_pos[k]
    if remain > ret:
        ret = remain
        last_max_index = k
    limit[k] = last_max_index


for j in range(n + 1):
    ans = max(ans, counter_clock_cumsum[j] - counter_clock_pos[j] * 2 + clock_cumsum[limit[n - j]] - clock_pos[
        limit[n - j]])



for m in range(n + 1):
    ans = max(ans, clock_cumsum[m] - clock_pos[m])


for p in range(n + 1):
    ans = max(ans, counter_clock_cumsum[p] - counter_clock_pos[p])


print(ans)