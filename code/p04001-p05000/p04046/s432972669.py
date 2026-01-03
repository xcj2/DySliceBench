class Combination:
    def __init__(self, size=100, mod=10**9 + 7):
        self.size = size + 2
        self.mod = mod
        self.fact = [1, 1] + [0] * size
        self.factInv = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size

        for i in range(2, size + 2):
            self.fact[i] = self.fact[i - 1] * i % mod
            self.inv[i] = -self.inv[mod % i] * (mod // i) % mod
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % mod

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % self.mod) % self.mod

def sol():
    H, W, A, B = map(int, input().split())
    MOD = 10**9 + 7

    comb = Combination(H + W + 100)

    ans = 0
    for i in range(W - B):
        ans = (ans + comb.ncr(H - 1 - A + B + i, H - 1 - A) * comb.ncr(A - 1 + W - 1 - B - i, A - 1)) % MOD

    print(ans)


sol()