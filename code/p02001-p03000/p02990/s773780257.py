from functools import reduce
class comb_mod:
    mod = 1000000007
    MAX = 10 ** 5
    fac = [0 for i in range(MAX)]
    finv = [0 for i in range(MAX)]
    inv = [0 for i in range(MAX)]

    def __init__(self):
        self.fac[0], self.fac[1] = 1, 1
        self.finv[0], self.finv[1] = 1, 1
        self.inv[1] = 1
        for i in range(2, self.MAX):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = self.mod - self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.mod
    def combination(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        return self.fac[n] * (self.finv[r] * self.finv[n - r] % self.mod) % self.mod
    def combination_mul(self, N, R):
        return reduce(lambda x, y: x * self.combination(y[0], y[1]) % self.mod, zip(N, R), 1)

def main():
    C = comb_mod()
    n, k = list(map(int, input().split()))
    for i in range(1, k + 1):
        N = [k - 1, n - k + 1]
        R = [i - 1, i]
        print(C.combination_mul(N, R))


if __name__ == '__main__':
    main()
