import sys
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)


class Comb(object):

    def __init__(self, n, MOD=1e9 + 7):
        self.MOD = MOD

        fac = [0] * (n + 10)
        finv = [0] * (n + 10)
        inv = [0] * (n + 10)

        fac[0] = 1
        fac[1] = 1
        finv[0] = 1
        finv[1] = 1
        inv[1] = 1

        for i in range(2, n + 10):
            fac[i] = fac[i - 1] * i % MOD
            inv[i] = MOD - inv[int(MOD % i)] * (MOD // i) % MOD
            finv[i] = finv[i - 1] * inv[i] % MOD
        self.fac = fac
        self.finv = finv
        self.inv = inv

    def calc_c(self, n, k):
        if n < k:
            return 0
        return self.fac[n] * (self.finv[k] * self.finv[n - k] %
                              self.MOD) % self.MOD

    def calc_h(self, n, k):
        return self.calc_c(n + k - 1, k)


MOD = 10**9 + 7
n, k = map(int, read().split())

comb = Comb(n, MOD)

ans = 0

for i in range(min(n, k) + 1):
    ans += comb.calc_c(n, i) * comb.calc_c(n - 1, i) % MOD

print(ans % MOD)
