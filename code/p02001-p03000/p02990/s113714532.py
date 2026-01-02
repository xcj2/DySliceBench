class Combination:
    def __init__(self, max_n, _mod):
        self.mod = _mod

        self.fac = [0 for _ in range(max_n + 10)]
        self.finv = [0 for _ in range(max_n + 10)]
        self.inv = [0 for _ in range(max_n + 10)]

        self.fac[0], self.fac[1] = 1, 1
        self.finv[0], self.finv[1] = 1, 1
        self.inv[1] = 1

        for i in range(2, max_n + 10):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = self.mod
            self.inv[i] -= self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.mod

    def mod_comb(self, n, k):
        if n < k or n < 0 or k < 0:
            return 0

        res = self.fac[n] * (self.finv[k] * self.finv[n - k] % self.mod)
        res %= self.mod

        return res


def main():
    max_n = 2000
    mod = 10**9 + 7
    comb = Combination(max_n, mod)

    N, K = map(int, input().split())
    for i in range(1, K + 1):
        a = comb.mod_comb(N - K + 1, i)
        b = comb.mod_comb(K - 1, i - 1)
        print(a * b % mod)


main()