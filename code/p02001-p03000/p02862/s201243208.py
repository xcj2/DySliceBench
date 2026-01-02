# https://atcoder.jp/contests/abc145/tasks/abc145_d


class Combination:                                      # 計算量は O(n_max + log(mod))
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max+1):                     # 階乗(= n_max !)の逆元を生成
            f = f * i % mod                             # 動的計画法による階乗の高速計算
            fac.append(f)                               # fac は階乗のリスト
        f = pow(f, mod-2, mod)                          # 階乗から階乗の逆元を計算。フェルマーの小定理より、　a^-1 = a^(p-2) (mod p) if p = prime number and p and a are coprime
                                                        # python の pow 関数は自動的に mod の下での高速累乗を行ってくれる
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):                   # 上記の階乗の逆元から階乗の逆元のリストを生成（＝ facinv ）
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()

    # "n 要素" は区別できる n 要素
    # "k グループ" はちょうど k グループ

    def __call__(self, n, r):  # self.C と同じ
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def C(self, n, r):
        if not 0 <= r <= n: return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

X, Y = map(int, input().split())

if (2*Y- X) % 3 or (2*X- Y) % 3:
    print(0)
    exit()

x = (2*Y - X) // 3
y = (2*X - Y) // 3

n = x + y
r = x


mod = 10**9 + 7
f = 1
for i in range(1, n + 1):
    f = f*i % mod
fac = f
f = pow(f, mod-2, mod)
facinv = [f]
for i in range(n, 0, -1):
    f = f*i % mod
    facinv.append(f)
facinv.append(1)

comb = Combination(n)
print(comb.C(n,r))