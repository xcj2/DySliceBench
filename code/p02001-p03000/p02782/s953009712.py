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


def main():
    MOD = 10 ** 9 + 7

    r1, c1, r2, c2 = map(int, input().split())

    cl = Calc(max_value=r2 + c2 + 1, mod=MOD)
    nCr = cl.nCr

    ans = 0
    for r in range(r1, r2 + 1):
        ans = (ans + nCr(r + c2 + 1, r + 1) - nCr(r + c1 - 1 + 1, r + 1)) % MOD
    print(ans)


if __name__ == '__main__':
    main()
