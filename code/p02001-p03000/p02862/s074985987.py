class Combination:
    """階乗とその逆元のテーブルをO(N)で事前作成し、組み合わせの計算をO(1)で行う"""
    def __init__(self, n, mod):
        self.fact = [1]
        for i in range(1, n + 1):
            self.fact.append(self.fact[-1] * i % mod)
        self.inv_fact = [0] * (n + 1)
        self.inv_fact[n] = pow(self.fact[n], mod - 2, mod)
        for i in reversed(range(n)):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % mod
        self.mod = mod

    def factorial(self, k):
        """k!を求める O(1)"""
        return self.fact[k]

    def inverse_factorial(self, k):
        """k!の逆元を求める O(1)"""
        return self.inv_fact[k]

    def permutation(self, k, r):
        """kPrを求める O(1)"""
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r]) % self.mod

    def combination(self, k, r):
        """kCrを求める O(1)"""
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r] * self.inv_fact[r]) % self.mod

    def combination_large(self, k, r):
        """kCrを求める O(r) kが大きいが、r <= nを満たしているときに使用"""
        if k < r:
            return 0
        res = 1
        for l in range(r):
            res *= (k - l)
            res %= self.mod
        return (res * self.inv_fact[r]) % self.mod



x, y = map(int, input().split())
mod = 10**9 + 7
comb = Combination(10**6,mod)

if (x+y)%3 != 0:
    print(0)
    exit(0)
i = (2*x-y)//3
j = (2*y-x)//3
n = i+j
r = i
if not 0 <= r <= n:
    print(0)
    exit(0)
print(comb.combination(n, r))
