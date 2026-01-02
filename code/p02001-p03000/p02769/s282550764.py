def e_roaming(MOD=10**9 + 7):
    N, K = [int(i) for i in input().split()]

    class Combination(object):
        """参考: https://harigami.net/contents?id=5f169f85-5707-4137-87a5-f0068749d9bb"""
        __slots__ = ['mod', 'factorial', 'inverse']

        def __init__(self, max_val_arg: int = 10**6, mod: int = 10**9 + 7):
            fac, inv = [1], []
            fac_append, inv_append = fac.append, inv.append

            for i in range(1, max_val_arg + 1):
                fac_append(fac[-1] * i % mod)

            # inv_append(pow(fac[-1], -1, mod)) (after Python 3.8)
            inv_append(pow(fac[-1], mod - 2, mod))

            for i in range(max_val_arg, 0, -1):
                inv_append((inv[-1] * i) % mod)

            self.mod, self.factorial, self.inverse = mod, fac, inv[::-1]

        def combination(self, n, r):
            r = min(r, n - r)
            if n < 0 or r < 0 or n < r:
                return 0
            return self.factorial[n] * self.inverse[r] * self.inverse[n - r] % self.mod

    comb = Combination(N).combination
    if K >= N:
        K = N - 1  # N 回以上移動することは、N-1 回移動することと同じ結果を生む
    return sum(comb(N, k) * comb(N - 1, k) % MOD for k in range(K + 1)) % MOD

print(e_roaming())