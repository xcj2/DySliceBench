from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]
dy8, dx8 = [0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


class Combination:
    def __init__(self, n, mod):
        assert 0 < n
        self.mod = mod
        self.fact = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, len(self.fact)):
            self.fact[i] = (i * self.fact[i - 1]) % self.mod
            self.inv[i] = pow(self.fact[i], self.mod - 2, self.mod)

    def nCr(self, n, k):
        if n == 0 and k == 0:
            return 1
        assert 0 <= n < len(self.fact) and 0 <= k
        a = self.fact[n]
        b = (self.inv[k] * self.inv[n - k]) % self.mod
        return a * b % self.mod


def main():
    H, W, A, B = map(int, input().split())
    MOD = 10 ** 9 + 7

    comb = Combination(100000 * 2 + 10, MOD)

    ans = 0
    for i in range(B + 1, W + 1):
        h, w = H - A - 1, i - 1
        s = comb.nCr(h + w, w) % MOD

        h, w = A - 1, W - i
        t = comb.nCr(h + w, w) % MOD

        ans += (s * t) % MOD
        ans %= MOD
    print(ans)



if __name__ == '__main__':
    main()
