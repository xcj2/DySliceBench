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


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007



n = I()
L = LI()
A = sorted(list(set(L)))
if len(A) == 1:
    if 1 <= A[0] <= n // 2 or A[0] == n - 1:
        print('Yes')
    else:
        print('No')
elif len(A) == 2 and A[0] + 1 == A[1]:
    cnt = Counter(L)
    min_type_num = cnt[min(L)]  + 1
    max_type_num = cnt[min(L)] + cnt[max(L)] // 2
    if min_type_num <= max(L) <= max_type_num:
        print('Yes')
    else:
        print('No')
else:
    print('No')