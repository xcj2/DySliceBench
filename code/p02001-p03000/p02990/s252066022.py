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
c = Combination(3000)

def H(n, r, mod=10**9+7):
    return c(n+r-1, r)


mod = 10**9+7
N, K = map(int, input().split())
B = K
R = N-K
for i in range(1, K+1):
    bn = i
    br = B-i
    rn = i+1
    rr = R-i+1
    if rr<0 or br<0:
        print(0)
    else:
        #print(i, bn, br, rn, rr)
        ans = H(bn, br) * H(rn, rr) % mod
        print(ans)
