import sys
import math
import fractions
import itertools
from collections import deque
import copy
import bisect

MOD = 10 ** 9 + 7
INF = 10 ** 18 + 7
input = lambda: sys.stdin.readline().strip()


def inv_mod(a, N):
    """
    Fermatの小定理より(Nが素数のときしか使えない)
    aの逆元 ax = 1 (mod N)を満たすx = a^(N-2) mod Nを返す。
    O(log N)
    """

    def bpm(x, y, N):
        """
         Bisection power method : 二分累乗法
         O(log y)でx^(y) mod N を求める。
        """
        ans = 1
        x %= MOD
        digit = int((math.log(y, 2) // 1 + 1))  # yの２進数表示の桁数
        for i in range(digit):
            if (y >> i) & 1 == 1:
                ans *= x
                ans %= MOD
            x **= 2
            x %= MOD
        return ans

    return bpm(a, N - 2, N)


def bpm(x, y, N):
    """
     Bisection power method : 二分累乗法
     O(log y)でx^(y) mod N を求める。
    """
    ans = 1
    x %= MOD
    digit = int((math.log(y, 2) // 1 + 1))  # yの２進数表示の桁数
    for i in range(digit):
        if (y >> i) & 1 == 1:
            ans *= x
            ans %= MOD
        x **= 2
        x %= MOD
    return ans


n, a, b = map(int, input().split())

nCa = 1
nCb = 1

inv_list = []

for i in range(max(a, b)):
    inv_list.append(inv_mod(i + 1, MOD))

for i in range(a):
    nCa *= inv_list[i]
    nCa %= MOD
    nCa *= n - i
    nCa %= MOD

for i in range(b):
    nCb *= inv_list[i]
    nCb %= MOD
    nCb *= n - i
    nCb %= MOD

print((bpm(2, n, MOD) - 1 - nCa - nCb) % MOD)
