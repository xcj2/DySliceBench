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


n = I()
red = sorted(LIR(n), key=lambda x:x[1], reverse=True)
blue = sorted(LIR(n))
red_used = [0] * n
for i in range(n):
    blue_x, blue_y = blue[i]
    for j in range(n):
        red_x, red_y = red[j]
        if red_x < blue_x and red_y < blue_y and not red_used[j]:
            red_used[j] = 1
            break


print(sum(red_used))