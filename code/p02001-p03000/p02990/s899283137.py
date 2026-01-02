MOD = 10 ** 9 + 7


class Combination:
    """
    初期化時に O(N) の計算を行っておくことで O(1) で nCk (mod MOD) の計算を行える
    """

    def __init__(self, N):
        self.fact = [1] * (N + 1)

        for i in range(1, N + 1):
            self.fact[i] = (self.fact[i - 1] * i) % MOD

        self.invmod = [1] * (N + 1)
        self.invmod[N] = pow(self.fact[N], MOD - 2, MOD)

        for i in range(N, 0, -1):
            self.invmod[i - 1] = (self.invmod[i] * i) % MOD

    def __call__(self, n, k):
        if n < 0 or k < 0 or n < k:
            return 0
        elif n == 0 or k == 0 or n == k:
            return 1
        else:
            return self.fact[n] * \
                (self.invmod[k] % MOD) * (self.invmod[n - k] % MOD)


def main():
    n, k = list(map(int, input().split()))
    cmb = Combination(2001)

    for i in range(1, k + 1):
        if i > n - k + 1 or i > k:
            print(0)
        else:
            ans = cmb(n - k + 1, i) * cmb(k - 1, i - 1) % MOD
            print(ans)


main()