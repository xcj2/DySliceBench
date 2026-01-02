import sys
sys.setrecursionlimit(300000)
class BinomialCoefficient(object):

    def __init__(self, N=510000, MOD=10**9+7):
        self.fac = [1, 1]
        self.finv = [1, 1]
        self.inv = [0, 1]
        self.MOD = MOD
        for i in range(2, N + 1):
            self.fac.append((self.fac[-1] * i) % MOD)
            self.inv.append((-self.inv[MOD % i] * (MOD // i)) % MOD)
            self.finv.append((self.finv[-1] * self.inv[-1]) % MOD)

    def C(self, n, r):
        if r < 0 or n < r:
            return 0
        return self.fac[n] * self.finv[r] * self.finv[n - r] % self.MOD

    def P(self, n, r):
        if r < 0 or n < r:
            return 0
        return self.fac[n] * self.finv[n - r] % self.MOD


def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M = MI()
bi = BinomialCoefficient()

ans = 0
for i in range(0, N + 1):
    sgn = (-1) ** i
    lans = bi.C(N, i) * bi.P(M - i, N - i) % MOD
    lans = lans * sgn
    ans = (ans + lans + MOD) % MOD

ans = ans * bi.P(M, N) % MOD
print(ans)