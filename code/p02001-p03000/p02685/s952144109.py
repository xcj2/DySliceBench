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


mod = 998244353
comb = combination(mod)
n, m, k = inpl()
if m == 1:
    if k >= n - 1:
        print(1)
        exit()
    else:
        print(0)
        exit()
ans = 0
for i in range(min(n, k + 1)):
    ans += m * pow(m - 1, n - 1 - i, mod) * comb.calc(n - 1, i) % mod
    ans %= mod
print(ans)
