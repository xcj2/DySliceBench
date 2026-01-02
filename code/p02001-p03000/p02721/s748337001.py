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

n, k, c = LI()
s = S()
l = [0] * n
r = [0] * n
a = c
x = 0
for i in range(n):
    a += 1
    if s[i] == 'o' and a > c:
        x += 1
        a = 0
    l[i] = x

l = [0] + l
a = c
x = 0
for j in range(n - 1, -1, -1):
    a += 1
    if s[j] == 'o' and a > c:
        x += 1
        a = 0
    r[j] = x

r = r + [0]
for m in range(n):
    if l[m] + r[m + 1] == k - 1:
        print(m + 1)