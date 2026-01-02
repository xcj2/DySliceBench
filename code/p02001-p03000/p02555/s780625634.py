from sys import stdin


class ModComb():
    def __init__(self, n_max, mod):
        self.fac = None
        self.mod = mod
        self.make_fac_table(n_max)

    def make_fac_table(self, n_max):
        self.fac = [1] + [0] * n_max
        for i in range(1, n_max + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod

    def mod_comb(self, n, k):
        if n == 0 and k == 0:
            return 1
        elif n < k or k < 0:
            return 0
        else:
            return self.fac[n] * pow(self.fac[n - k], self.mod - 2, self.mod) * \
                pow(self.fac[k], self.mod - 2, self.mod) % self.mod

    def mod_comb_with_rep(self, n, k):
        return self.mod_comb(n + k - 1, k)


def main():
    _in = [_.rstrip() for _ in stdin.readlines()]
    S = int(_in[0])  # type:int
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    ans = 0
    MOD = 10**9 + 7
    modcomb = ModComb(S + 1, MOD)
    min_ = 1
    max_ = S // 3
    for i in range(min_, max_ + 1):
        res = S - i * 3
        ans += modcomb.mod_comb_with_rep(res + 1, i - 1)
        ans %= MOD
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(ans)


if __name__ == "__main__":
    main()