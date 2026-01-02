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


n, k = LI()
A = [0] + LI()



for i in range(1, n + 1):
    A[i] = (A[i] + A[i - 1]) % k


for i in range(n + 1):
    A[i] = (A[i] - i) % k



ans = 0
D = defaultdict(int)
for j in range(n, -1, -1):
    ans += D[A[j]]
    D[A[j]] += 1
    if j + k - 1 < n + 1:
        D[A[j + k - 1]] -= 1


if k == 1:
    print(0)
else:
    print(ans)