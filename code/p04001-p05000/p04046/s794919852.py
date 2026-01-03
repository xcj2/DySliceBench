def d_iroha_and_a_grid(MOD=10**9 + 7):
    class Combination(object):
        """参考: https://harigami.net/contents?id=5f169f85-5707-4137-87a5-f0068749d9bb"""
        __slots__ = ["mod", "factorial", "inverse"]

        def __init__(self, max_n: int = 10**6, mod: int = 10**9 + 7):
            fac, inv = [1], []
            fac_append, inv_append = fac.append, inv.append

            for i in range(1, max_n + 1):
                fac_append(fac[-1] * i % mod)

            inv_append(pow(fac[-1], mod - 2, mod))

            for i in range(max_n, 0, -1):
                inv_append(inv[-1] * i % mod)

            self.mod, self.factorial, self.inverse = mod, fac, inv[::-1]

        def comb(self, n, r):
            if n < 0 or r < 0 or n < r:
                return 0
            return self.factorial[n] * self.inverse[r] * self.inverse[n - r] % self.mod

    H, W, A, B = [int(i) for i in input().split()]
    c = Combination(max_n=H + W)
    # 左上のマスの座標を(0,0)としたとき、B<=i<=W-1を満たすiについて、
    # (0,0)→(H-A-1,i)への行き方 * (H-A-1,i)→(H-A,i)への行き方(1通り) *
    # (H-A,i)→(H-1,W-1)への行き方 の値の総和を取る(10**9+7で剰余を取る)
    ans = sum([c.comb(H - A - 1 + i, H - A - 1)
               * c.comb(A - 1 + W - 1 - i, A - 1) for i in range(B, W)])
    return ans % MOD

print(d_iroha_and_a_grid())