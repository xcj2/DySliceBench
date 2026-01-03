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
x = LI() + [INF]
l = I()
q = I()
db = [[0] * n for _ in range(31)]
now = 0
for i in range(n):
    while x[i] + l >= x[now + 1]:
        now += 1
    db[0][i] = now

for j in range(1, 31):
    for k in range(n):
        db[j][k] = db[j - 1][db[j - 1][k]]

for _ in range(q):
    a, b = LI()
    if a > b:
        a, b = b, a
    a -= 1
    b -= 1
    ret = 0
    for kk in range(30, -1, -1):
        if db[kk][a] < b:
            a = db[kk][a]
            ret += 2 ** kk
    print(ret + 1)



