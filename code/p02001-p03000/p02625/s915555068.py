import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m = map(int,readline().split())
mod = 10**9+7

class Combination:
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max+1):
            f = f * i % mod
            fac.append(f)
        f = pow(f, mod-2, mod)
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def C(self, n, r):
        if not 0 <= r <= n: return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def P(self, n, r):
        if not 0 <= r <= n: return 0
        return self.fac[n] * self.facinv[n-r] % self.mod
      
f = Combination(m, mod)
ans = 0
for k in range(m+1):
  chk = f.C(n,k)*f.P(m,k)*pow(f.P(m-k,n-k),2,mod)%mod
  ans += pow(-1,k)*chk
  ans %= mod
print(ans)