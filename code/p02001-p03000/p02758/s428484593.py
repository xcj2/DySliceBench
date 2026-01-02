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
from copy import deepcopy

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
mod = 998244353

class Segtree:
    def __init__(self, A, ide_ele, segfunc, initialize=True):
        self.n = len(A)
        self.size = 2 ** (self.n - 1).bit_length()
        self.ide_ele = ide_ele
        self.segfunc = segfunc
        if initialize:
            self.data = [ide_ele] * self.size + A + [ide_ele] * (self.size - self.n)
            for i in range(self.size - 1, 0, -1):
                self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])
        else:
            self.data = [ide_ele] * (2 * self.size)

    def update(self, k, x):
        k += self.size
        self.data[k] = x
        while k > 0:
            k = k >> 1
            self.data[k] = self.segfunc(self.data[2 * k], self.data[2 * k + 1])

    def query(self, l, r):
        L, R = l + self.size, r + self.size
        s = self.ide_ele
        while L < R:
            if R & 1:
                R -= 1
                s = self.segfunc(s, self.data[R])
            if L & 1:
                s = self.segfunc(s, self.data[L])
                L += 1
            L >>= 1
            R >>= 1
        return s


n = I()
XD = sorted(LIR(n))
X = []
D = []
for x, d in XD:
    X += [x]
    D += [d]

last = [l for l in range(n)]
st = Segtree(last, -INF, max)
for i in range(n - 2, -1, -1):
    r = bisect_left(X, X[i] + D[i])
    ret = st.query(i, r)
    st.update(i, ret)
    last[i] = ret

dp = [1] * (n + 1)
for j in range(n - 1, -1, -1):
    k = last[j]
    dp[j] = (dp[j + 1] + dp[k + 1]) % mod


print(dp[0])
