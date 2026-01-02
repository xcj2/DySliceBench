def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD=10 ** 9 + 7

def combination(n, r, mod=10**9+7):
    n1, r = n+1, min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod


class BinomialCoefficient(object):

    def __init__(self, N=510000, MOD=10**9+7):
        self.fac = [1, 1]
        self.finv = [1, 1]
        self.inv = [0, 1]
        self.MOD = MOD
        for i in range(2, N + 1):
            self.fac.append((self.fac[-1] * i) % MOD)
            self.inv.append((-self.inv[MOD % i] * (MOD // i)) % MOD)
            self.finv.append((self.finv[-1] * self.inv[-1]) % MOD)

    def comb(self, n, r):
        if r < 0 or n < r or r < 0:
            return 0
        return self.fac[n] * self.finv[r] * self.finv[n - r] % self.MOD



n, k = MI()

if k >= n:
    print(combination(2 * n - 1, n, MOD))
    exit(0)

coef = BinomialCoefficient(n + 1, MOD)
ans = 1
for l in range(1, k + 1):
    ans += coef.comb(n, l) * coef.comb(n - 1, l)
    ans %= MOD
print(ans % MOD)
