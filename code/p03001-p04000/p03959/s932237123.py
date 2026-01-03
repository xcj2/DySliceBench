from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
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
mod = 10 ** 9 + 7


n = I()
T = LI()
A = LI()
flg = [0] * n
pre = 0
for i in range(n):
    if T[i] > pre:
        flg[i] = 1
        pre = T[i]

pre = 0
for j in range(n - 1, -1, -1):
    if A[j] == pre:
        if flg[j]:
            if T[j] > A[j]:
                print(0)
                exit()
        else:
            T[j] = min(T[j], A[j])
    else:
        if flg[j] and T[j] != A[j]:
            print(0)
            exit()
        else:
            if A[j] > T[j]:
                print(0)
                exit()
            else:
                T[j] = A[j]
                flg[j] = 1
                pre = A[j]

ans = 1
for k in range(n):
    if flg[k] == 0:
        ans = ans * T[k] % mod

print(ans)