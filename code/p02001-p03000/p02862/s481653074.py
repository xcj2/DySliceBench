MAX = 5100000

MOD = 1000000007


def read_input():
    x, y = map(int, input().split(" "))
    return x, y


class BinomialCoefficients(object):
    def __init__(self, MAX=MAX, MOD=MOD):
        self.MOD = MOD
        self.fac = [1 for _ in range(MAX)]
        self.finv = [1 for _ in range(MAX)]
        self.inv = [1 for _ in range(MAX)]
        for i in range(2, MAX):
            self.fac[i] = self.fac[i - 1] * i % MOD
            self.inv[i] = MOD - self.inv[MOD % i] * (MOD // i) % MOD
            self.finv[i] = self.finv[i - 1] * self.inv[i] % MOD

    def calc(self, n, k):
        if n < k:
            return 0
        if n == 0 or k < 0:
            return 0
        return self.fac[n] * (self.finv[k] * self.finv[n - k] % self.MOD) % self.MOD


def ans(X, Y):
    a_3 = 2 * X - Y
    b_3 = 2 * Y - X
    if a_3 % 3 != 0 and b_3 % 3 != 0:
        return 0
    if a_3 < 0 or b_3 < 0:
        return 0
    a = a_3 // 3
    b = b_3 // 3

    c = BinomialCoefficients()
    return c.calc(a + b, a)


if __name__ == "__main__":
    X, Y = read_input()
    print(ans(X, Y))
