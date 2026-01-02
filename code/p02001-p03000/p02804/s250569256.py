def e_max_min_sums(MOD=10**9 + 7):
    N, K = [int(i) for i in input().split()]
    A = sorted([int(i) for i in input().split()])

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

    comb = Combination(N + 1).combination
    ans = 0
    for time in range(2):  # time == 1 のときは min を計算している
        for i in range(N):
            current = comb(i, K - 1)
            if time == 1:
                current = -current
            ans += A[i] * current
        A.reverse()
    return ans % MOD

print(e_max_min_sums())