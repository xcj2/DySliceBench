from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce
from copy import deepcopy

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


n = I()
L = [[[0]]]
for i in range(1, n):
    new_L = []
    for each_type in L:
        new_L += [each_type + [[i]]]
        for j in range(len(each_type)):
            new_type = deepcopy(each_type)
            new_type[j] += [i]
            new_L += [new_type]
    L = new_L


ans = []
for t in L:
    a = [''] * n
    cnt = 97
    for k in t:
        for l in k:
            a[l] = chr(cnt)
        cnt += 1
    ans += [''.join(a)]


for i in sorted(ans):
    print(i)

