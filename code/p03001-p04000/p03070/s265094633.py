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
INF = 10 ** 18
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
mod = 998244353


n = I()
A = IR(n)



a_sum = sum(A)
dp1 = [0] * (a_sum + 1)
dp1[0] = 1
dp2 = [0] * (a_sum + 1)
dp2[0] = 1
for i in range(n):
    for j in range(a_sum, -1, -1):
        if j < A[i]:
            dp2[j] = dp2[j] * 2 % mod
        else:
            dp1[j] = (dp1[j] + dp1[j - A[i]]) % mod
            dp2[j] = (dp2[j] * 2 + dp2[j - A[i]]) % mod


ans = pow(3, n, mod)
for k in range((a_sum + 1) // 2, a_sum + 1):
    ans = (ans - dp2[k] * 3) % mod


if a_sum % 2 == 0:
    ans = (ans + dp1[a_sum // 2] * 3) % mod


print(ans)