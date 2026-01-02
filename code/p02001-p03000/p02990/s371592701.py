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
    nCr = nCrMod(mod)
    N, K = map(int, input().split())
    r = 0
    for i in range(1, K + 1):
        if i - 1 > N - K:
            print(0)
            continue
        print(nCr(K - 1, i - 1) * nCr(N - K + 1, i) % mod)
main()
