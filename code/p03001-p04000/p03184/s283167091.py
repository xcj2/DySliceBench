
class Combination:
    def __init__(self, n_max, mod=10 ** 9 + 7):
        # O(n_max + log(mod))
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max + 1):
            f = f * i % mod
            fac.append(f)
        f = pow(f, mod - 2, mod)
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()

    # "n 要素" は区別できる n 要素
    # "k グループ" はちょうど k グループ

    def __call__(self, n, r):  # self.C と同じ
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def nCr(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod


def resolve():
    MOD = 10 ** 9 + 7
    H, W, N = map(int, input().split())
    wall = []
    for _ in range(N):
        r, c = map(lambda x: int(x) - 1, input().split())
        wall.append((r, c))
    # 番兵
    wall.append((H - 1, W - 1))
    wall.sort()

    cmb = Combination((H + W) + 1)
    dp = [0] * (N + 1)

    # 壁がない時(0,0)から(x,y)まで移動する場合の数: x+yCx
    # dp[i] =f(r[i]+c[i],c[i])−(i−1番目までの壁に1回以上ぶつかって壁iの位置にたどり着く場合の数)
    for i in range(N + 1):
        r1, c1 = wall[i]
        dp[i] = cmb.nCr(r1 + c1, c1)
        for j in range(0, i):
            dx = r1 - wall[j][0]
            dy = c1 - wall[j][1]
            # dp[j]: 1～j-1 番目の壁を避けてj番目の壁の位置にたどり着く場合の数
            # nCr :  j 番目の壁の位置からi番目の壁の位置まで壁を無視して移動する場合の数
            tmp = dp[j] * cmb.nCr(dx + dy, dy)
            dp[i] = (dp[i] - tmp % MOD + MOD) % MOD

    print(dp[N])


if __name__ == "__main__":
    resolve()