def d_factorization(MOD=10**9 + 7):
    N, M = [int(i) for i in input().split()]

    def prime_factorization_dict(n):
        if n == 1:
            return {2: 0}  # 1は素数の0乗の積とみなす
        i, table = 2, {}
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
        """参考: https://harigami.net/contents?id=5f169f85-5707-4137-87a5-f0068749d9bb"""
        __slots__ = ['mod', 'factorial', 'inverse']

        def __init__(self, max_val_arg: int = 10**6, mod: int = 10**9 + 7):
            fac, inv = [1], []
            fac_append, inv_append = fac.append, inv.append

            for i in range(1, max_val_arg + 1):
                fac_append(fac[-1] * i % mod)

            inv_append(pow(fac[-1], mod - 2, mod))

            for i in range(max_val_arg, 0, -1):
                inv_append((inv[-1] * i) % mod)

            self.mod, self.factorial, self.inverse = mod, fac, inv[::-1]

        def combination(self, n, r):
            if n < 0 or r < 0 or n < r:
                return 0
            return self.factorial[n] * self.inverse[r] * self.inverse[n - r] % self.mod

        def combination_with_repetition(self, n, r):
            return self.combination(n + r - 1, r)

    prime_m = prime_factorization_dict(M)
    h = Combination(max(prime_m.values()) + N - 1).combination_with_repetition
    ans = 1
    for b in prime_m.values():
        ans = (ans * h(N, b)) % MOD
    return ans

print(d_factorization())