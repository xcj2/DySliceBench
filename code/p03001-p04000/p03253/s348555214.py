def d_factorization(N, M):
    def prime_factorization_dict(n):
        if n == 1:
            return {2: 0}  # 1は素数の0乗の積とみなす
        i = 2
        table = {}
        while i**2 <= n:
            table[i] = 0
            while n % i == 0:
                table[i] += 1
                n //= i
            if table[i] == 0:
                table.pop(i)
            i += 1
        if n > 1:
            table[n] = 1
        return table

    class Combination(object):
        def __init__(self, n, mod):
            self.mod = mod
            # フェルマーの小定理による組合せの計算
            self.factorial = [1] * (n + 1)  # 0!からn!の結果を格納
            for k in range(1, n):
                self.factorial[k + 1] = (self.factorial[k] * (k + 1)) % mod
            # k!のmodにおける逆元を計算
            self.fact_inv = [1] * (n + 1)
            self.fact_inv[n] = pow(self.factorial[n], mod - 2, mod)
            for k in reversed(range(1, n + 1)):
                self.fact_inv[k - 1] = (self.fact_inv[k] * k) % mod

        def comb(self, n, r):
            if n < 0 or r < 0 or n < r:
                return 0
            return (self.factorial[n] * self.fact_inv[r] * self.fact_inv[n - r]) % self.mod

        def comb_with_repetition(self, n, r):
            if n == 0 and r > 0:
                return 0
            if n >= 0 and r == 0:
                return 1
            return self.comb(n + r - 1, r)

    MOD = 10**9 + 7
    prime_m = prime_factorization_dict(M)
    c = Combination(max(prime_m.values()) + N - 1, MOD)
    ans = 1
    for b in prime_m.values():
        ans = (ans * c.comb_with_repetition(N, b)) % MOD

    return ans

N, M = [int(i) for i in input().split()]
print(d_factorization(N, M))