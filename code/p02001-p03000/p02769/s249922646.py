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
    n, k = map(int, input().split())
    mf = modfact(n)
    res = 0
    for i in range(min(k + 1, n)):
        res += mf.comb(n, i) * mf.comb(n - 1, i) % MOD
        res %= MOD
    print(res)
resolve()