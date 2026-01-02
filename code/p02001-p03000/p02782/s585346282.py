import sys
sys.setrecursionlimit(2147483647)
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()

class modfact(object):
    def __init__(self, n):
        fact, invfact = [1] * (n + 1), [1] * (n + 1)
        for i in range(1, n + 1): fact[i] = i * fact[i - 1] % MOD
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1): invfact[i] = invfact[i + 1] * (i + 1) % MOD
        self._fact, self._invfact = fact, invfact

    def inv(self, n):
        return self._fact[n - 1] * self._invfact[n] % MOD

    def fact(self, n):
        return self._fact[n]

    def invfact(self, n):
        return self._invfact[n]

    def comb(self, n, k):
        if k < 0 or n < k: return 0
        return self._fact[n] * self._invfact[k] % MOD * self._invfact[n - k] % MOD

    def perm(self, n, k):
        if k < 0 or n < k: return 0
        return self._fact[n] * self._invfact[n - k] % MOD

def resolve():
    r1, c1, r2, c2 = map(int, input().split())
    mf = modfact(r2 + c2 + 2)
    def S(m, n):
        res = (m + 2) * mf.comb(m + n + 2, m + 2) % MOD * mf.inv(n + 1) % MOD
        res -= 1
        return res % MOD

    res = S(r2, c2) - S(r1 - 1, c2) - S(r2, c1 - 1) + S(r1 - 1, c1 - 1)
    print(res % MOD)
resolve()