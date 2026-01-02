N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
MOD = 10**9+7
# 各aが何回最大最小として選ばれるか考える
ans = 0

class Combination:

    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def make_factorial_list(self, n):
        # 階乗のリストと階乗のmod逆元のリストを返す O(n)
        # self.make_modinv_list()が先に実行されている必要がある
        fac = [1]
        facinv = [1]
        for i in range(1, n+1):
            fac.append(fac[i-1] * i % self.mod)
            facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        # 0からnまでのmod逆元のリストを返す O(n)
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
        return modinv

comb = Combination(N+1)

for i in range(N):
    if i >= K-1:
        ans += (A[i] * comb(i,K-1))%MOD
        ans %= MOD


for i in range(N):
    if i <= N-K:
        ans -= (A[i] * comb(N-1-i,K-1))%MOD
        ans %= MOD
print(ans)