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
mod = 998244353


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
        while x:
            res += self.bit[x - 1]
            x -= x & -x
        return res


n = I()
X = []
Y = []
XY = []
for x, y in LIR(n):
    Y += [y]
    X += [x]

co_to_ind = {e: i for i, e in enumerate(sorted(Y))}
Y = [co_to_ind[k] for k in Y]
Y = [Y[i] for i in sorted(range(n), key=lambda j:X[j])]
pow2 = [1]
for i in range(n):
    pow2 += [pow2[-1] * 2 % mod]


ans = pow2[n - 1] * n % mod
bit = BIT(n)
for i, y in enumerate(Y):
    bit.add(y, 1)
    ld = bit.sum(y - 1)
    lu = i - ld
    rd = y - ld
    ru = n - y - 1 - lu
    ans = ans + (pow2[ld] - 1) * (pow2[ru] - 1) % mod * pow2[lu] % mod * pow2[rd] % mod + (pow2[lu] - 1) * \
          (pow2[rd] - 1) % mod * pow2[ld] % mod * pow2[ru] % mod - (pow2[ld] - 1) * (pow2[ru] - 1) % mod * \
          (pow2[rd] - 1) % mod * (pow2[lu] - 1) % mod


print(ans % mod)




