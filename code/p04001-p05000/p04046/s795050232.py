def examD(mod):
    class combination():
        def __init__(self, n, mod):
            self.n = n
            self.fac = [1] * (n + 1)
            self.inv = [1] * (n + 1)
            for j in range(1, n + 1):
                self.fac[j] = self.fac[j - 1] * j % mod

            self.inv[n] = pow(self.fac[n], mod - 2, mod)
            for j in range(n - 1, -1, -1):
                self.inv[j] = self.inv[j + 1] * (j + 1) % mod

        def comb(self, n, r, mod):
            if r > n or n < 0 or r < 0:
                return 0
            return self.fac[n] * self.inv[n - r] * self.inv[r] % mod

    H, W, A, B =LI()
    N = H + W
    C = combination(N,mod)
    ans = C.comb(W+H-B-2, H-1,mod)
    pre = 1
    for i in range(1, H-A):
        ans += (C.comb(B+i,i,mod)-pre)*C.comb(W+H-B-2-i, H-1-i,mod)%mod
        ans %= mod
        pre = C.comb(B+i, i,mod)
    print(ans)

import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD(mod)