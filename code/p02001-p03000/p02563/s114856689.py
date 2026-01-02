#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from heapq import heappush, heappop, heapify

import itertools
import math, fractions
import sys, copy

def L(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline().rstrip())
def SL(): return list(sys.stdin.readline().rstrip())
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def R(n): return [sys.stdin.readline().strip() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if len(args) > 0 else [default for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 1000000007
INF = float("inf")

sys.setrecursionlimit(1000000)

class NTT:
    '''
        conv: ci = ∑_{j=0}^i a_j * b_{i−j} % mod
        添字の和がiになるajとbkの積の和
    '''

    def __init__(self, a, b, mod=998244353, root=3):
        self.mod, self.root = mod, root
        deg = len(a) + len(b) - 2
        self.n = deg.bit_length()
        N = 1 << self.n
        self.roots  = [pow(self.root, (self.mod-1)>>i, self.mod) for i in range(24)] # 1 の 2^i 乗根
        self.iroots = [pow(x,self.mod-2,self.mod) for x in self.roots] # 1 の 2^i 乗根の逆元

        self.conv = a + [0]*(N-len(a))
        self.b = b + [0]*(N-len(b))

        self.untt()
        self.untt(False)
        for i in range(N):
            self.conv[i] = self.conv[i] * self.b[i] % self.mod
        self.iuntt()
        del self.conv[deg+1:] # inplace ver. of self.conv[:deg+1]

    def untt(self, flag=True):
        a = self.conv if flag else self.b
        for i in range(self.n):
            m = 1 << (self.n - i - 1)
            for s in range(1 << i):
                W = 1
                s *= m * 2
                for p in range(m):
                    a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m]) % self.mod, (a[s+p]-a[s+p+m]) * W % self.mod
                    W = W * self.roots[self.n-i] % self.mod

    def iuntt(self):
        for i in range(self.n):
            m = 1 << i
            for s in range(1 << (self.n-i-1)):
                W = 1
                s *= m * 2
                for p in range(m):
                    self.conv[s+p], self.conv[s+p+m] = (self.conv[s+p]+self.conv[s+p+m]*W)%self.mod, (self.conv[s+p]-self.conv[s+p+m]*W)%self.mod
                    W = W * self.iroots[i+1] % self.mod
        inv = pow((self.mod + 1) // 2, self.n, self.mod)
        for i in range(1<<self.n):
            self.conv[i] = self.conv[i] * inv % self.mod


def main():
    N, M = LI()
    a = LI()
    b = LI()
    ntt = NTT(a, b)
    print(*ntt.conv)

if __name__ == '__main__':
    main()