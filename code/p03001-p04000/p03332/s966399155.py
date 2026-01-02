mod = 998244353


class Combination:
    """
    SIZEが10^6程度以下の二項係数を何回も呼び出したいときに使う
    使い方:
    comb = Combination(SIZE, MOD)
    comb(10, 3) => 120
    """

    def __init__(self, N, MOD=10 ** 9 + 7):
        self.MOD = MOD
        self.fact, self.inv = self._make_factorial_list(N)

    def __call__(self, n, k):
        if k < 0 or k > n:
            return 0
        res = self.fact[n] * self.inv[k] % self.MOD
        res = res * self.inv[n - k] % self.MOD
        return res

    def _make_factorial_list(self, N):
        fact = [1] * (N + 1)
        inv = [1] * (N + 1)
        MOD = self.MOD
        for i in range(1, N + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        inv[N] = pow(fact[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            inv[i - 1] = (inv[i] * i) % MOD
        return fact, inv


if __name__ == "__main__":
    N, A, B, K = map(int, input().split())
    U = 3 * 10 ** 5 + 10
    comb = Combination(U, mod)

    ans = 0
    if A > B:
        A, B = B, A
    for i in range(N + 1):
        X = A * i
        if X > K:
            continue
        if (K - X) % B != 0:
            continue
        if (K - X) // B > N:
            continue
        j = (K - X) // B

        red = comb(N, i)
        blue = comb(N, j)
        ans = (ans + red * blue % mod) % mod
    print(ans)