MOD = 998244353

m = 2*10**5 + 10
fac = [0] * m
finv = [0] * m
inv = [0] * m


class modint():
    def __init__(self, value):
        self.value = value % MOD

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return (modint(self.value + other.value) if isinstance(other, modint)
                else modint(self.value + other))

    def __sub__(self, other):
        return (modint(self.value - other.value) if isinstance(other, modint)
                else modint(self.value - other))

    def __mul__(self, other):
        return (modint(self.value * other.value) if isinstance(other, modint)
                else modint(self.value * other))

    def __truediv__(self, other):
        return (modint(self.value * pow(other.value, MOD - 2, MOD))
                if isinstance(other, modint)
                else modint(self.value * pow(other, MOD - 2, MOD)))

    def __pow__(self, other):
        return (modint(pow(self.value, other.value, MOD))
                if isinstance(other, modint)
                else modint(pow(self.value, other, MOD)))

    def __eq__(self, other):
        return (self.value == other.value if isinstance(other, modint)
                else self.value == (other % MOD))

    def __ne__(self, other):
        return (self.value == other.value if isinstance(other, modint)
                else self.value == (other % MOD))

    def __radd__(self, other):
        return (modint(other.value + self.value) if isinstance(other, modint)
                else modint(other + self.value))

    def __rsub__(self, other):
        return (modint(other.value - self.value) if isinstance(other, modint)
                else modint(other - self.value))

    def __rmul__(self, other):
        return (modint(other.value * self.value) if isinstance(other, modint)
                else modint(other * self.value))

    def __rtruediv__(self, other):
        return (modint(other.value * pow(self.value, MOD - 2, MOD))
                if isinstance(other, modint)
                else modint(other * pow(self.value, MOD - 2, MOD)))

    def __rpow__(self, other):
        return (modint(pow(other.value, self.value, MOD))
                if isinstance(other, modint)
                else modint(pow(other, self.value, MOD)))

    def modinv(self):
        return modint(pow(self.value, MOD - 2, MOD))


def COMBinitialize(m):
    fac[0] = 1
    finv[0] = 1
    if m > 1:
        fac[1] = 1
        finv[1] = 1
        inv[1] = 1
        for i in range(2, m):
            fac[i] = fac[i-1] * i % MOD
            inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
            finv[i] = finv[i - 1] * inv[i] % MOD


def COMB(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


COMBinitialize(m)


def main():
    N, M, K = (int(i) for i in input().split())
    ans = modint(0)
    for i in range(K+1):
        cur = M*pow(M-1, (N-1-i), MOD)*COMB(N-1, i)
        ans += cur
    print(ans)


if __name__ == '__main__':
    main()
