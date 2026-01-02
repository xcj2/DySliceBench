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



n, m = LI()
ret = [''] * n
for _ in range(m):
    s, c = LI()
    if ret[s - 1] and ret[s - 1] != str(c):
        print(-1)
        exit()
    elif s == 1 and c == 0 and n != 1:
        print(-1)
        exit()
    else:
        ret[s - 1] = str(c)

for i in range(n):
    if not ret[i]:
        ret[i] = '0' if i or n == 1 else '1'

ans = ''.join(ret)
print(ans)