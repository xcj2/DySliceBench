import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

class modfact(object):
    def __init__(self, n):
        fact, invfact = [1] * (n + 1), [1] * (n + 1)
        for i in range(1, n + 1): fact[i] = i * fact[i - 1] % MOD
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1): invfact[i] = invfact[i + 1] * (i + 1) % MOD
        self._fact, self._invfact = fact, invfact

    def fact(self, n):
        return self._fact[n]

    def invfact(self, n):
        return self._invfact[n]

    def comb(self, n, k):
        return self._fact[n] * self._invfact[k] % MOD * self._invfact[n - k] % MOD if 0 <= k <= n else 0

    def perm(self, n, k):
        return self._fact[n] * self._invfact[n - k] % MOD if 0 <= k <= n else 0

def resolve():
    n = int(input())
    mf = modfact(n)
    ans = 0
    for k in range(n):
        ans += mf.comb(n - 1 - 2 * k, k - 1)
    print(ans % MOD)
resolve()