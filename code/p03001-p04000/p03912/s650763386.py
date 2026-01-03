from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
from re import split
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce
from copy import deepcopy
import re

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


n, m = LI()
X = LI()
D = defaultdict(lambda:defaultdict(int))
for k in X:
    D[k % m][k] += 1

ans = 0
if m % 2 == 0:
    ans += sum(D[m // 2].values()) // 2

ans += sum(D[0].values()) // 2

for i in range(1, (m + 1) // 2):
    x = D[i].values()
    y = D[m - i].values()
    if sum(x) > sum(y):
        x, y = y, x
    x_sum = sum(x)
    y_sum = sum(y)
    ans += x_sum
    ret = 0
    for j in y:
        ret += j // 2 * 2
        if ret > y_sum - x_sum:
            ans += (y_sum - x_sum) // 2
            break
    else:
        ans += ret // 2

print(ans)






