class combination():
    #素数のmod取るときのみ　速い
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


import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = int(0)

N, M, K = LI()

cou = int(0)
#maxL = N + M -2
L = int(0)
#距離i+1の組み合わせ

#for i in range(maxL):
for j in range(N):
    L += (N - j - 1) * (M ** 2) * (j + 1)
    L %= mod
for j in range(M):
    L += (M - j - 1) * (N ** 2) * (j + 1)
    L %= mod
#    for j in range(i+2):
#        if i>1 and i+1>j>0:
#            L[i] += max((N-j)*(M-(1+i)+j),0)*(i+1)*2
#        else:
#            L[i] += max(((N - j) * (M - (1 + i) + j)), 0) * (i + 1)
C = combination(N*M-2,mod)
cou = C.comb(N*M-2,K-2,mod)*L%mod

print(cou)