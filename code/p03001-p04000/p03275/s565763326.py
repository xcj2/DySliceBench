from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left, bisect_right
import random
from itertools import permutations, accumulate, combinations
import sys
import string



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
mod = 10 ** 9 + 7


n = I()
A = LI()


class BIT:
    def __init__(self, size):
        self.bit = [0] * size
        self.size = size

    def add(self, i, w):
        x = i + 1
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        return

    def sum(self, i):
        res = 0
        x = i + 1
        while x > 0:
            res += self.bit[x - 1]
            x -= x & -x
        return res



def D(L):
    n = len(L)
    bit = BIT(2 * n + 1)
    ans = 0
    for i in range(n - 1, -1, -1):
        bit.add(L[i] + n, 1)
        ans += bit.sum(L[i] + n - 1)
    return ans



ALL = (n + 1) * n // 2
A2 = sorted(A)
# 求めるのは、1より-1の方が多かった区間の数
ng, ok = n, 0
while ng > ok + 1:
    mid = (ok + ng) // 2
    L = [0] + list(accumulate([1 if i >= A2[mid] else -1 for i in A]))
    if D(L) >= ALL // 2 + 1:
        ng = mid
    else:
        ok = mid


print(A2[ok])




