# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

class Mint(object):
    def cmb(self, n, r, mod: int = 10 ** 9 + 7):
        if (r < 0) or (r > n):
            return 0
        r = min(r, n - r)
        return self.g1[n] * self.g2[r] * self.g2[n - r] % mod

    def cmb_prep(self, N: int, mod: int = 10 ** 9 + 7):
        self.g1 = [1, 1]  # 元テーブル
        self.g2 = [1, 1]  # 逆元テーブル
        inverse = [0, 1]  # 逆元テーブル計算用テーブル

        for i in range(2, N + 1):
            self.g1.append((self.g1[-1] * i) % mod)
            inverse.append((-inverse[mod % i] * (mod // i)) % mod)
            self.g2.append((self.g2[-1] * inverse[-1]) % mod)

    def cmb_(n, r):
        """ 普通にnCrを求める
        >>> p = Mint()
        >>> p.cmb_(10, 2)
        45
        """
        from operator import mul
        from functools import reduce

        r = min(n - r, r)
        if r == 0:
            return 1
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1, r + 1))
        return over // under


mod = 10**9 + 7
x, y = map(int, input().split())

if (2 * y -x) % 3 != 0:
    print(0)
    sys.exit()

if (2 * x -y) % 3 != 0:
    print(0)
    sys.exit()

n = (2 * y -x) // 3
m = (2* x -y) // 3

mint = Mint()
mint.cmb_prep(n + m, mod)

print(mint.cmb(n+m, n, mod))
