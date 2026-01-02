from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd, sqrt
from operator import mul
from functools import reduce
from operator import mul
from pprint import pprint



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


n = int(input())
a = list(map(int, input().split()))
c = a[0] + a[1]

t = 0
flg = 0

for ai in a[2:]:
    t = t ^ ai

if c < t:
    flg = 1

if (c - t) % 2:
    flg = 1

b1 = (c - t) // 2

a1 = b1

if a1 > a[0]:
    print(-1)
    sys.exit()

for i in reversed(range((a[0] + a[1]).bit_length())):
    if t & (1 << i):
        if b1 & (1 << i):
            print(-1)
            sys.exit()
        if a1 + 2 ** i <= a[0]:
            a1 += 2 ** i

if a1 == 0:
    flg = 1

print(a[0] - a1 if flg == 0 else -1)









