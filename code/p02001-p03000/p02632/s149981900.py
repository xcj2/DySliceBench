class Calc:
    def __init__(self, max_value, mod):
        """combination(max_value, all)"""
        fact = [-1] * (max_value + 1)
        fact[0] = 1
        fact[1] = 1
        for x in range(2, max_value + 1):
            fact[x] = x * fact[x - 1] % mod

        invs = [1] * (max_value + 1)
        invs[max_value] = pow(fact[max_value], mod - 2, mod)
        for x in range(max_value - 1, 0, -1):
            invs[x] = invs[x + 1] * (x + 1) % mod

        self.fact = fact
        self.invs = invs
        self.mod = mod

    def nCr(self, n, r):
        r = min(n - r, r)
        if r < 0: return 0
        if r == 0: return 1
        if r == 1: return n
        return self.fact[n] * self.invs[r] * self.invs[n - r] % self.mod

    def nHr(self, n, r):
        return self.nCr(n - 1 + r, r)


class PowPreCalc:
    def __init__(self, *, b, m, mod):
        """(b**m)%mod"""
        res = [1]
        t = 1
        for _ in range(m):
            t = t * b % mod
            res.append(t)
        self._res = res

    def get_pow(self, m):
        """(b**m)%mod"""
        return self._res[m]


def main():
    MOD = 10 ** 9 + 7

    K = int(input())
    S = input()

    N = len(S)

    calc = Calc(max_value=N - 1 + K, mod=MOD)

    p26 = PowPreCalc(b=26, m=K, mod=MOD)
    p25 = PowPreCalc(b=25, m=K, mod=MOD)

    ans = 0
    for tail_len in range(K + 1):
        ans = (ans
               + calc.nCr(N - 1 + K - tail_len, N - 1) * p26.get_pow(tail_len) * p25.get_pow(K - tail_len)
               ) % MOD

    print(ans)


if __name__ == '__main__':
    main()
