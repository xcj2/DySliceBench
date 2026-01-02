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



def bi_search(k):
    ok = 0
    ng = n // k + 1
    while ng > ok + 1:
        mid = (ng + ok) // 2
        if calc(mid, k):
            ok = mid
        else:
            ng = mid
    return ok


def calc(x, k):
    # x回できるか?
    l = bisect_left(L, (x, 0))
    # 全部使えるのが左側、l回しか使えないのが右側。
    if kv_acc[l - 1] + acc[l] * x >= k * x:
        return True
    else:
        return False




n = I()
A = LI()
L = [(0, 0)] + sorted([(k, v) for k, v in Counter(Counter(A).values()).items()])
m = len(L)
acc = [0] * (m + 1)
for i in range(m - 1, -1, -1):
    acc[i] = acc[i + 1] + L[i][1]

kv_acc = list(accumulate([k * v for k, v in L]))
for k in range(1, n + 1):
    print(bi_search(k))


