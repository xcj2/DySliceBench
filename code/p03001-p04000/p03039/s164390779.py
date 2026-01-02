import sys
s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in ss]
ss2nnn = lambda ss: [s2nn(s) for s in ss]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline().rstrip() for _ in range(n)]
ii2sss = lambda n: [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))

MOD = int(1e+9) + 7

def comb(n, k):
    r = 1
    for i in range(n, max(n-k, k), -1):
        r *= i
    for i in range(1, min(n-k, k) + 1, 1):
        r //= i
    return r

class Comb:
    def __init__(self, MAX, MOD):
        MAX += 1
        fac = [0] * MAX
        finv = [0] * MAX
        inv = [0] * MAX
        fac[0] = fac[1] = 1
        finv[0] = finv[1] = 1
        inv[1] = 1
        for i in range(2, MAX):
            fac[i] = fac[i - 1] * i % MOD
            inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
            finv[i] = finv[i - 1] * inv[i] % MOD
        self.fac = fac
        self.finv = finv
        self.MOD = MOD
    
    def comb(self, n, k):
        fac = self.fac
        finv = self.finv
        MOD = self.MOD
        if (n < k):
            return 0
        if (n < 0 or k < 0):
            return 0
        return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

def main():
    # 行数, 列数, 駒数
    N, M, K = i2nn()
    # 配置コストの総和 % MOD

    # 例）N, M, K = 2, 2, 2
    # 駒が置ける場所は4箇所: N * M
    # 駒の配置は6通り: comb(4, 2) = comb(N*M, K)
    # K=2 の場合のコスト
    xcost = 0
    for i in range(1, M):
        # iをx座標の差とする
        # x座標のみに注目した場合、差がiとなるのは(M-i)通り
        #   M=4, i=1, => (1,2), (2,3), (3,4) = 3通り
        #   M=4, i=2, => (1,3), (2,4) = 2通り
        #   M=4, i=3, => (1,4) = 1通り
        # さらにy座標の組み合わせは, 左側がN通り, 右側がN通り
        #   (1,2) について M=2 の場合 ((1,1), (2,1)), ((1,1), (2,2)), ((1,2), (2,1)), ((1,2), (2,2))
        xcost = (xcost + i * (M-i) * (N*N)) % MOD
    ycost = 0
    for i in range(1, N):
        ycost = (ycost + i * (N-i) * (M*M)) % MOD
    cost = (xcost + ycost) % MOD
    # K=3 の場合、K=2 の場合のコストを NM-2 倍すればよい
    # 汎用的に考えると、 K=2 の場合のコストを comb(MN-2, K-2) 倍すればよい
    #cost = (cost * comb(M*N-2, K-2)) % MOD
    cost = (cost * Comb(N*M-2, MOD).comb(N*M-2, K-2)) % MOD
    print(cost)

main()
