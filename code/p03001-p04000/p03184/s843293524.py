
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
    def route(a, b):
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        if dx < 0 or dy < 0:
            return 0
        return cmb.nCr(dx+dy, dx)


    MOD = 10 ** 9 + 7
    H, W, N = map(int, input().split())
    wall = []
    for _ in range(N):
        r, c = map(lambda x:int(x)-1, input().split())
        wall.append((r, c))
    # スタート位置
    wall.append((0, 0))
    wall.sort()

    cmb = Combination((H + W) + 1)
    dp = [[0] * 2 for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(0, i):
            dp[i][0] += dp[j][1] * route(wall[j], wall[i]) % MOD
            dp[i][0] %= MOD
            dp[i][1] += dp[j][0] * route(wall[j], wall[i]) % MOD
            dp[i][1] %= MOD

    goal = (H-1, W-1)
    ng = 0
    for i in range(1, N+1):
        ng -= dp[i][0] * route(wall[i], goal) % MOD
        ng += dp[i][1] * route(wall[i], goal) % MOD
        ng %= MOD

    # 全体 - ng
    all = cmb.nCr(H+W-2, H-1)
    ans = (all - ng + MOD) % MOD
    print(ans)


if __name__ == "__main__":
    resolve()
