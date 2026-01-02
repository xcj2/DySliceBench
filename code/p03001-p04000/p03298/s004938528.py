from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, cos, radians, pi, sin
from operator import mul
from functools import reduce
from operator import mul


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
mod = 10 ** 9 + 7


n = I()
s = S()
s1 = s[:n]
s2 = s[n:][::-1]
D1 = defaultdict(int)
D2 = defaultdict(int)
for i in range(2 ** n):
    a1 = ""
    b1 = ""
    for j in range(n):
        if i >> j & 1:
            a1 += s1[j]
        else:
            b1 += s1[j]
    D1[(a1, b1)] += 1

for i in range(2 ** n):
    a2 = ""
    b2 = ""
    for j in range(n):
        if i >> j & 1:
            a2 += s2[j]
        else:
            b2 += s2[j]
    D2[(a2, b2)] += 1

ret = 0
for i in D1:
    ret += D1[i] * D2[i]

print(ret)





