class Combination:
    def __init__(self, N: int, MOD: int):
        fac = [0 for _ in range(N + 1)]
        fac[0] = 1
        for i in range(1, N + 1):
            fac[i] = fac[i - 1] * i % MOD
        self.fac = fac
        self.N = N
        self.MOD = MOD

    def _modpow(self, x: int, n: int) -> int:
        ret = 1
        while n > 0:
            if n % 2 == 1:
                ret = ret * x % self.MOD
            x = x * x % self.MOD
            n >>= 1
        return ret

    def _modinv(self, x: int) -> int:
        return self._modpow(x, self.MOD - 2)

    def combination(self, n: int, k: int) -> int:
        if n < k:
            return 0
        return self.fac[n] * self._modinv(self.fac[k]) % self.MOD * self._modinv(self.fac[n - k]) % self.MOD

N, A, B = map(int, input().split())
MOD = int(1e9) + 7
S = 2 ** N % MOD

comb = Combination(3 * int(1e5), MOD)


def f(X):
    x = 1
    for i in range(1, X + 1):
        x *= comb._modinv(i)
        x *= (N - i + 1)
        x %= MOD

    return x

S += 3 * MOD - f(A) - f(B) - 1
S %= MOD
print(S)