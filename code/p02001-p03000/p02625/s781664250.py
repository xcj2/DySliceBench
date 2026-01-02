class PrimeTool():
    def __init__(self, max=5 * 10 ** 5 + 500, mod=10 ** 9 + 7):
        self.mod = mod
        self.modm2 = self.mod - 2
        self.max = max
        self.fac = [1] * max
        self.inv = [1] * max
        if self.max > 1:
            for i in range(2, self.max):
                self.fac[i] = (self.fac[i - 1] * i) % self.mod
                self.inv[i] = pow(self.fac[i], self.modm2, self.mod)

    def perm(self, n, r):
        if r == 0:
            return 1
        return self.fac[n] * self.inv[n - r] % self.mod

    def cmb(self, n, r):
        r = max(r, n - r)
        if n == r:
            return 1
        return self.fac[n] * self.inv[n - r] * self.inv[r] % self.mod


def resolve():
    N, M = map(int, input().split(' '))
    res = 0
    tool = PrimeTool()

    for k in range(N + 1):
        res += (-1) ** k * tool.cmb(N, k) * tool.perm(M, k) * tool.perm(M - k, N - k) ** 2
        res %= tool.mod

    print(res)


resolve()