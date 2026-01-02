class Combination:
    def __init__(self, size, mod=10**9 + 7):
        self.size = size + 2
        self.mod = mod
        self.fact = [1, 1] + [0] * size
        self.factInv = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size

        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % self.mod
            self.inv[i] = -self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % self.mod

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % self.mod

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % self.mod) % self.mod

    def factN(self, n):
        if n < 0:
            return 0
        return self.fact[n]

    def f(self, p, q):
        return self.fact[p + q] * self.factInv[p] * self.factInv[q] % MOD


X, Y = map(int, input().split())
MOD = 10**9 + 7

if (X + Y) % 3 != 0:
    print(0)
    exit()

time = (X + Y) // 3
ans = 0
comb = Combination(time + 10)

for y in range(time + 1):
    x = time - y

    if X == x * 2 + y and Y == y * 2 + x:
        ans += comb.f(x, y)
        ans %= MOD

print(ans % MOD)