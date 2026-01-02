import sys
input = sys.stdin.readline

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

    def __call__(self, n, r):  # self.C と同じ
        if not 0 <= r <= n: return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def H(self, n, r):                                  # (箱区別:〇　ボール区別:×　空箱:〇)　重複組み合わせ nHm
        if (n == 0 and r > 0) or r < 0: return 0
        return self.fac[n+r-1] * self.facinv[r] % self.mod * self.facinv[n-1] % self.mod


n, k = map(int, input().split())
MOD = 10**9 + 7
C = Combination(n)

k = min(k,n-1)
res = 0
for l in range(k+1):
    res += C(n,l)*C.H(n-l,l)
print(res%MOD)
