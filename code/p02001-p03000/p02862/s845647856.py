def d_knight():
    X, Y = [int(i) for i in input().split()]

    if (abs(X) + abs(Y)) % 3 != 0 or Y > 2 * X or 2 * Y < X:
        return 0

    n = (abs(X) + abs(Y)) // 3
    k = -1
    for x in range(n, 2 * n + 1):
        if Y == 3 * n - x:
            k = x - n
            break

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
    return Combination().combination(n, k)

print(d_knight())