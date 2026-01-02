#!/usr/bin/python3
# import bisect
# from collections import Counter, deque, OrderedDict, defaultdict
# from copy import copy, deepcopy # pythonのみ．copyは1次元，deepcopyは多次元．
# from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import statistics # Pythonのみ
# import string
import unittest
from io import StringIO
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    n, m, K = map(int, input().split())
    class Combination:
        """階乗とその逆元のテーブルをO(N)で事前作成し、組み合わせの計算をO(1)で行う"""

        def __init__(self, n, MOD):
            self.fact = [1]
            for i in range(1, n + 1):
                self.fact.append(self.fact[-1] * i % MOD)
            self.inv_fact = [0] * (n + 1)
            self.inv_fact[n] = pow(self.fact[n], MOD - 2, MOD)
            for i in reversed(range(n)):
                self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % MOD
            self.MOD = MOD

        def factorial(self, k):
            """k!を求める O(1)"""
            return self.fact[k]

        def inverse_factorial(self, k):
            """k!の逆元を求める O(1)"""
            return self.inv_fact[k]

        def permutation(self, k, r):
            """kPrを求める O(1)"""
            if k < r:
                return 0
            return (self.fact[k] * self.inv_fact[k - r]) % self.MOD

        def combination(self, k, r):
            """kCrを求める O(1)"""
            if k < r:
                return 0
            return (self.fact[k] * self.inv_fact[k - r] * self.inv_fact[r]) % self.MOD

        def combination2(self, k, r):
            """kCrを求める O(r) kが大きいが、r <= nを満たしているときに使用"""
            if k < r:
                return 0
            res = 1
            for l in range(r):
                res *= (k - l)
                res %= self.MOD
            return (res * self.inv_fact[r]) % self.MOD
    MOD = 998244353
    comb = Combination(10 ** 6, MOD)

    ans = 0
    df=m*pow(m-1,n-1-K,MOD)

    now = df
    for i in range(K, -1, -1):
        now = comb.combination(n-1, i)
        ans += now*df
        ans %= MOD
        df *= (m-1)
        df%=MOD

    print(ans)

resolve()