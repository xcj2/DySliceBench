# !/usr/bin/env python3
import sys
from operator import itemgetter
# gcd
# from fractions import gcd
# 切り上げ，切り捨て
# from math import ceil, floor
# リストの真のコピー（変更が伝播しない）
# from copy import deepcopy
# 累積和。list(accumulate(A))としてAの累積和
# from itertools import accumulate
# l = ['a', 'b', 'b', 'c', 'b', 'a', 'c', 'c', 'b', 'c', 'b', 'a']
# S = Counter(l)  # カウンタークラスが作られる。S=Counter({'b': 5, 'c': 4, 'a': 3})
# print(S.most_common(2))  # [('b', 5), ('c', 4)]
# print(S.keys())  # dict_keys(['a', 'b', 'c'])
# print(S.values())  # dict_values([3, 5, 4])
# print(S.items())  # dict_items([('a', 3), ('b', 5), ('c', 4)])
# from collections import Counter
# import math
# from functools import reduce
#
# input関係の定義
# fin = open('in_3.txt', 'r')
# sys.stdin = fin
# 提出時はコメントアウト+上のshebangを有効にする
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args): return print(*args, file=sys.stderr)
# template

MOD = 1000000007  # type: int

def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word

class Modint():
    '''
    自動でMODで割った余りを計算してくれる整数。MODは素数である必要があり，デフォルトは10**9+7。

    Parameters
    ----------
        n (int) : Modintの初期値
        MOD=10^9+7 (int) : 余りを計算するMOD。素数である必要がある。

    Methods
    ----------
        inverse(n: int) -> Modint
            n の逆元を返す。
    '''

    def __init__(self, n: int, mod=MOD):
        if n >= 0:
            self.n = n % mod
        else:
            self.n = (mod - (-n) % mod) % mod
        self.mod = mod

    def __eq__(self, other):
        return self.n == int(other)

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        return self.__class__(-self.n)

    def __str__(self):
        return str(self.n)

    def __int__(self):
        return self.n

    def __iadd__(self, other):
        self.n += int(other)
        self.n %= self.mod
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        self.n -= int(other)
        self.n %= self.mod
        return self

    def __rsub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        self.n = self.n * int(other) % self.mod
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def inverse(self):
        '''
        フェルマーの小定理を考えると，MOD-2乗することでMODでの逆元を求めることができる。これは組み込み関数のpowを使うと十分に早い（O(log MOD)）。
        '''
        return self.__class__(pow(self.n, self.mod - 2, self.mod))

    def __ifloordiv__(self, other):
        self *= pow(int(other), self.mod - 2, self.mod)
        return self

    def __rfloordiv__(self, other):
        return self.__class__(other).__floordiv__(self)

    def __add__(self, other):
        return self.__class__(self.n + int(other))

    def __sub__(self, other):
        return self.__class__(self.n - int(other))

    def __mul__(self, other):
        return self.__class__(self.n * int(other))

    def __floordiv__(self, other):
        return self.__class__(self.n * Modint(int(other)).inverse())

    # def comb(self, n: int, k: int):
    #     '''
    #     コンビネーション絡みの定義。comb(n,k):特に前処理をせずnCkを求める
    #     毎回O(N)かかるので死ぬ覚悟でO(N^2)を投げるくらいしか無理

    #     ちなみにですが，これでABC132_D()を出すとPyPy3で1932msくらいですれすれセーフ
    #     '''
    #     if n < k or k < 0:
    #         return Modint(0)
    #     res = Modint(1)
    #     for i in range(int(k)):
    #         res *= Modint(n - i)
    #         res //= Modint(i + 1)
    #     return res

    # def H(self, n: int, k: int):
    #     if n < 0 or k < 0:
    #         return Modint(0)
    #     elif n == 0 and k == 0:
    #         return Modint(1)
    #     else:
    #         return self.comb(n + k - 1, n)


COMBINATION_MAX = 2 * 10**5
class Combination():
    def __init__(self, sz=COMBINATION_MAX):
        '''
        Nまでの階乗とその逆元（割り算用）を計算しておく。前処理にO(N)，P, C, Hそれぞれの計算はO(1)。N = 200000なら割と余裕で通る。
        '''
        self._fact = [Modint(0)] * (sz + 1)
        self._rfact = [Modint(0)] * (sz + 1)
        self._fact[0] = Modint(1)
        self._rfact[sz] = Modint(1)
        for i in range(1, sz + 1):
            self._fact[i] = self._fact[i - 1] * Modint(i)
        self._rfact[sz] = self._fact[sz].inverse()
        for i in range(sz - 1, -1, -1):
            self._rfact[i] = self._rfact[i + 1] * Modint(i + 1)

    def fact(self, k: int) -> int:
        """階乗の計算"""
        return self._fact[k]

    def rfact(self, k: int) -> int:
        """階乗の逆元の計算"""
        return self._rfact[k]

    def P(self, n: int, k: int) -> Modint:
        '''
        nPkの値を返す。nはあらかじめ前処理されたN以下でないとダメ

        Parameters
        ----------
            n (int) : nPkのn (0<=n<=N)
            k (int) : nPkのk （0<=k<=n）

        Returns
        ----------
            Modint : nPkをModint型で返す。Modintに依存。
        '''
        if k < 0 or n < k:
            return Modint(0)
        return self._fact[n] * self._rfact[n - k]

    def C(self, n: int, k: int) -> Modint:
        '''
        nCkの値を返す。nはあらかじめ前処理されたN以下でないとダメ

        Parameters
        ----------
            n (int) : nCkのn(0<=n<=N)
            k (int) : nCkのk（0<=k<=n）

        Returns
        ----------
            Modint : nCkをModint型で返す。Modintに依存。
        '''
        if k < 0 or n < k:
            return Modint(0)
        if n - k < k:
            k = n - k
        return self._fact[n] * self._rfact[k] * self._rfact[n - k]

    def H(self, n: int, k: int) -> Modint:
        '''
        nHkの値を返す。nはあらかじめ前処理された n+k-1 以下でないとダメ

        ちなみにnHkはn個の区別できないものをk個の箱に分けるパターンの数で，結局n+k-1Cnになる。

        Parameters
        ----------
            n (int) : nHkのn(0<=n<=N)
            k (int) : nHkのk（0<=k<=n）

        Returns
        ----------
            Modint : nHkをModint型で返す。Modintに依存。
        '''
        if n < 0 or k < 0:
            return Modint(0)
        elif k == 0:
            return Modint(1)
        return self.C(n + k - 1, k)

# END CUT HERE

if __name__ == '__main__':

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = {int(next(tokens)) for _ in range(M)}  # type: "List[int]"

    # write code
    issafe = [True for i in range(N + 10)]
    for i in a:
        issafe[i] = False
    dp = [Modint(0) for i in range(N + 10)]
    dp[0] = Modint(1)
    if issafe[1]:
        dp[1] = Modint(1)
    for n in range(2, N + 2):
        if issafe[n - 1]:
            dp[n] += dp[n - 1]
            debug(n, "!")
        if issafe[n - 2]:
            dp[n] += dp[n - 2]
            debug(n, "?")
    print(dp[N])
