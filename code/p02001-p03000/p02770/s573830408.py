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
import pprint
sys.setrecursionlimit(10 ** 9)


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



k, q = LI()
D = LI()
for _ in range(q):
    n, x, m = LI()
    ret = x
    D_m = [d % m for d in D]
    zero_or_one = [0] + list(accumulate([1 if d == 0 else 0 for d in D_m]))
    Dm_acc = [0] + list(accumulate(D_m))
    ret = x + (n - 1) // k * Dm_acc[-1] + Dm_acc[(n - 1) % k]
    zero_ret = (n - 1) // k * zero_or_one[-1] + zero_or_one[(n - 1) % k]
    print(n - 1 - (ret // m - x // m) - zero_ret)