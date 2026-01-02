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

n = I()
A = []
B = []
for _ in range(n):
    s = S()
    ret = 0
    ret2 = 0
    for i in s:
        if ret and i == ')':
            ret -= 1
        elif i == '(':
            ret += 1
        else:
            ret2 += 1
    if ret2 > ret:
        A += [(ret, ret2)]
    else:
        B += [(ret, ret2)]

A.sort()
B.sort(key=lambda x:x[1], reverse=True)
L = A + B
now = 0
for x, y in L:
    if x > now:
        print('No')
        exit()
    now = now - x + y

if now:
    print('No')
else:
    print('Yes')




