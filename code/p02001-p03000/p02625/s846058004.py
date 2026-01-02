class nCrMod():
    def __init__(self, mod):
        self.mod = mod
        self.fac = [1, 1]
        self.finv = [1, 1]
        self.inv = [0, 1]

    def prep(self, n):
        mod = self.mod
        f, fi = self.fac[-1], self.finv[-1]
        for i in range(len(self.fac), n + 1):
            fn = f * i % mod
            v = -self.inv[mod % i] * (mod // i) % mod
            fin = fi * v % mod
            f, fi = fn, fin
            self.fac.append(f)
            self.finv.append(fi)
            self.inv.append(v)

    def __call__(self, n, r):
        if len(self.fac) <= n:
            self.prep(n)
        return self.fac[n] * self.finv[r] * self.finv[n - r] % self.mod


def main():
    N, M = map(int, input().split())
    mod = 10**9 + 7
    nCr = nCrMod(mod)
    nPr = lambda n, r: nCr(n, r) * nCr.fac[r] % mod
    r = nPr(M, N) ** 2 % mod
    for i in range(1, N + 1):
        r = (r + (-1)**i * nCr(N, i) * nPr(M, i) * (nPr(M - i, N - i) ** 2)) % mod
    return r % mod

print(main())
