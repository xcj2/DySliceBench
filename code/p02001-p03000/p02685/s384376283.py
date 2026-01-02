n, m, k = map(int, input().split())


class Combination:
    """
    comb = Combination(1000000)
    print(comb(5, 3))  # 10
    """
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def make_factorial_list(self, n):
        fac = [1]
        facinv = [1]
        for i in range(1, n+1):
            fac.append(fac[i-1] * i % self.mod)
            facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
        return modinv


mod = 998244353
total = 0
comb = Combination(n, mod)

v2 = [0] * (k+1)
v2[k] = (m * pow(m-1, n-k-1, mod)) % mod
for i in range(k-1, -1, -1):
    v2[i] = (v2[i+1] * (m-1)) % mod

for i in range(k+1):
    v = comb(n-1, i)
    total += (v * v2[i]) % mod
    total %= mod

print(total)