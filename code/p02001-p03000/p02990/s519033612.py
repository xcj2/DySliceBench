import sys

input = lambda: sys.stdin.readline().rstrip()
mod = 10**9 + 7


class Combination:
    """
    O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    comb = Combination(1000000)
    print(comb(5, 3))  # 10
    """

    def __init__(self, n_max, mod=10**9 + 7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def make_factorial_list(self, n):
        fac = [1]
        facinv = [1]
        for i in range(1, n + 1):
            fac.append(fac[i - 1] * i % self.mod)
            facinv.append(facinv[i - 1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        modinv = [0] * (n + 1)
        modinv[1] = 1
        for i in range(2, n + 1):
            modinv[i] = self.mod - self.mod // i * modinv[self.mod % i] % self.mod
        return modinv


def solve():
    N, K = map(int, input().split())
    blue = K
    red = N - K
    comb = Combination(2000, mod)

    # i == 0
    print(red + 1)

    # i >= 1
    for i in range(1, blue):
        c = comb(blue - 1, i)
        t = 0
        for j in range(i - 1, red):
            t += comb(j, i - 1) * (red - j)
            t %= mod
        ans = (c * t) % mod
        print(ans)


if __name__ == '__main__':
    solve()
