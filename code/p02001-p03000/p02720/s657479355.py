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

def check(a):
    for l in range(len(a) - 1):
        if not -1 <= a[l] - a[l + 1] <= 1:
            return False
    return True

x = [0]
k = I()
ret = 0
j = len(x) - 1
while True:
    if x == [9] * len(x):
        x = [1] + [0] * len(x)
        ret += 1
        j = len(x) - 1
        if ret == k:
            print(''.join([str(m) for m in x]))
            exit()
    if j and (x[j - 1] + 1 == x[j] or x[j] == 9):
        j -= 1
        continue
    x[j] += 1
    for n in range(j + 1, len(x)):
        x[n] = x[n - 1] - 1 if x[n - 1] else 0
    j = len(x) - 1
    ret += 1
    if ret == k:
        print(''.join([str(m) for m in x]))
        exit()
