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
from functools import reduce


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
# def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n = I()
s = S()
q = I()
def f(k):
    cnt = [0, 0, 0] # dの個数、mの個数、dmの個数
    ans = 0
    for i in range(n):
        if i - k >= 0:
            if s[i - k] == 'D':
                cnt[2] -= cnt[1]
                cnt[0] -= 1
            elif s[i - k] == 'M':
                cnt[1] -= 1
        if s[i] == 'D':
            cnt[0] += 1
        elif s[i] == 'M':
            cnt[1] += 1
            cnt[2] += cnt[0]
        elif s[i] == 'C':
            ans += cnt[2]
    return ans

K = LI()
for i in range(q):
    print(f(K[i]))
