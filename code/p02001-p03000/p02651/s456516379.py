from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce
from operator import mul


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
mod = 1000000007




def least_bit_set(x):
    return x & (-x)


def delete_zeros_from(values, start):
    i = start
    for j in range(start, len(values)):
        if values[j] != 0:
            values[i] = values[j]
            i += 1
    del values[i:]


def eliminate(values):
    values = list(values)
    i = 0
    while True:
        delete_zeros_from(values, i)
        if i >= len(values):
            return values
        j = i
        for k in range(i + 1, len(values)):
            if least_bit_set(values[k]) < least_bit_set(values[j]):
                j = k
        values[i], values[j] = (values[j], values[i])
        for k in range(i + 1, len(values)):
            if least_bit_set(values[k]) == least_bit_set(values[i]):
                values[k] ^= values[i]
        i += 1


def in_span(x, eliminated_values):
    for y in eliminated_values:
        if least_bit_set(y) & x != 0:
            x ^= y
    return x == 0


t = I()
for _ in range(t):
    n = I()
    A = LI()
    s = S()
    flg = 0
    values = []
    for j in range(n - 1, -1, -1):
        if int(s[j]) == 0:
            values += [A[j]]
            values = eliminate(values)
        else:
            if not in_span(A[j], values):
                print(1)
                break
    else:
        print(0)






