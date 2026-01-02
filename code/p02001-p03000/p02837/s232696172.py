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


n = I()
testimony = [[] for _ in range(n)]
for i in range(n):
    a = I()
    testimony[i] = LIR(a)


ans = 0
for j in range(2 ** n - 1, -1, -1):
    flag = 0
    bit_cnt = 0
    for k in range(n):
        if j >> k & 1:
            bit_cnt += 1
            for x, y in testimony[k]:
                if y != j >> (x - 1) & 1:
                    flag = 1
                    break
            if flag:
                break
    else:
        ans = max(ans, bit_cnt)


print(ans)