from bisect import bisect_right, bisect_left

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

    def nhr(self, n, r):  # 重複組合せ
        return self.ncr(n + r - 1, n - 1)

    def factN(self, n):
        if n < 0:
            return 0
        return self.fact[n]

N, K = map(int, input().split())
MOD = 10**9 + 7
comb = Combination(N + 100)
A = list(map(int, input().split()))
A.sort()

ans = 0
for i, a in enumerate(A):
    mi = min(i, bisect_right(A, a) - 1)
    mx = N - max(i + 1, bisect_left(A, a))

    ans = (ans + (comb.ncr(mi, K - 1) - comb.ncr(mx, K - 1)) * a) % MOD

print(ans)