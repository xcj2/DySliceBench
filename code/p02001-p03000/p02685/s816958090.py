import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 998244353
INF = float('inf')

class BinomialCoefficient(object):

    def __init__(self, N=210000, MOD=998244353):
        self.fac = [1, 1]
        self.finv = [1, 1]
        self.inv = [0, 1]
        self.MOD = MOD
        for i in range(2, N + 1):
            self.fac.append((self.fac[-1] * i) % MOD)
            self.inv.append((-self.inv[MOD % i] * (MOD // i)) % MOD)
            self.finv.append((self.finv[-1] * self.inv[-1]) % MOD)

    def comb(self, n, r):
        if r < 0 or n < r or r < 0:
            return 0
        return self.fac[n] * self.finv[r] * self.finv[n - r] % self.MOD

coef = BinomialCoefficient()

N, M, K = MI()
ans = 0
for l in range(K + 1):
    lans = pow(M - 1, N - l - 1, MOD)
    lans = M * lans % MOD
    lans = lans * coef.comb(N - 1, l) % MOD
    ans = (ans + lans) % MOD
print(ans)