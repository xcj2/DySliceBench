import math

def factor(n):
    i = 2
    r = []
    while i * i <= n:
        if n % i == 0:
            c = 0
            while n % i == 0:
                c += 1
                n //= i
            r.append((i, c))
        i += 1
    if n > 1:
        r.append((n, 1))
    return r

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
    f = factor(M)
    r = 1
    for p, q in f:
        r = r * nCr(N + q - 1, q) % mod
    return r

print(main())
