from itertools import accumulate


class Combination:
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
    N, K = map(int, input().split())
    MOD = 10**9+7
    comb = Combination(2*10**5+5, MOD)

    ans = []
    for i in range(min(N - 1, K) + 1):
        val = comb(N, i) * comb(N - 1, i) % MOD
        ans.append(val)

    answer = 0
    while ans:
        answer = (answer + ans.pop()) % MOD
    print(answer)
