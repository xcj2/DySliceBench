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
    mod = 10 ** 9 + 7
    ncr = nCrMod(mod)

    r1, c1, r2, c2 = map(int, input().split())
    r1, c1 = r1 - 1, c1 - 1
    t = ncr(r2 + c2 + 2, c2 + 1) + ncr(r1 + c1 + 2, c1 + 1) - ncr(r1 + c2 + 2, c2 + 1) - ncr(r2 + c1 + 2, c1 + 1)
    print(t % mod)

main()
