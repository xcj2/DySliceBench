import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7


def inp():
    '''
    一つの整数
    '''
    return int(input())


def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


def str_inp():
    '''
    文字列をリストとして読み込む
    '''
    return list(input()[:-1])


class combination():
    def __init__(self, mod):
        '''
        modを指定して初期化
        '''
        self.mod = mod
        self.fac = [1, 1]  # 階乗テーブル
        self.ifac = [1, 1]  # 階乗の逆元テーブル
        self.inv = [0, 1]  # 逆元計算用

    def calc(self, n, k):
        '''
        nCk%modを計算する
        '''
        if k < 0 or n < k:
            return 0
        self.make_tables(n)  # テーブル作成
        k = min(k, n - k)
        return self.fac[n] * (self.ifac[k] * self.ifac[n - k] %
                              self.mod) % self.mod

    def make_tables(self, n):
        '''
        階乗テーブル・階乗の逆元テーブルを作成
        '''
        for i in range(len(self.fac), n + 1):
            self.fac.append((self.fac[-1] * i) % self.mod)
            self.inv.append(
                (-self.inv[self.mod % i] * (self.mod // i)) % self.mod)
            self.ifac.append((self.ifac[-1] * self.inv[-1]) % self.mod)


k = inp()
s = str_inp()
comb = combination(mod)
ans = pow(26, len(s) + k, mod)
for i in range(0, len(s)):
    ans -= comb.calc(k + len(s), i) * pow(25, k + len(s) - i, mod)
    ans %= mod
print(ans)
