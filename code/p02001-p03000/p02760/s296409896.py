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
mod = 1000000007


A = LIR(3)
n = I()
for _ in range(n):
    a = I()
    for i in range(3):
        for j in range(3):
            if A[i][j] == a:
                A[i][j] = 0

flg = 0
for i in range(3):
    if not sum(A[i]):
        flg = 1

for i in range(3):
    ret = 0
    for j in range(3):
        ret += A[j][i]
    if ret == 0:
        flg = 1

ret = 0
for i in range(3):
    ret += A[i][i]
if ret == 0:
    flg = 1

ret = 0
for i in range(3):
    ret += A[i][2 - i]

if ret == 0:
    flg = 1


if flg:
    print('Yes')
else:
    print('No')

