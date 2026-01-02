from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor


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



s = S()
ans = 0
i = len(s) - 1
a_cnt = 0
bc_cnt = 0
while i >= 0:
    if s[i-1:i+1] == 'BC':
        i -= 2
        bc_cnt += 1
    elif s[i] == 'A':
        i -= 1
        a_cnt += 1
        ans += bc_cnt
    else:
        a_cnt = bc_cnt = 0
        i -= 1




print(ans)