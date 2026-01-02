import sys
INF = 1 << 60
MOD = 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

prime = 998244353
root = 3
def _fmt(A, inverse = False):
    N = len(A)
    logN = (N - 1).bit_length()
    base = pow(root, (prime - 1) // N * (1 - 2 * inverse) % (prime - 1), prime)
    step = N
    for k in range(logN):
        step >>= 1
        w = pow(base, step, prime)
        wj = 1
        nA = [0] * N
        for j in range(1 << k):
            for i in range(1 << logN - k - 1):
                s, t = i + j * step, i + j * step + (N >> 1)
                ps, pt = i + j * step * 2, i + j * step * 2 + step
                nA[s], nA[t] = (A[ps] + A[pt] * wj) % prime, (A[ps] - A[pt] * wj) % prime
            wj = (wj * w) % prime
        A = nA
    return A

def convolution(f, g):
    N = 1 << (len(f) + len(g) - 2).bit_length()
    Ff, Fg = _fmt(f + [0] * (N - len(f))), _fmt(g + [0] * (N - len(g)))
    N_inv = pow(N, prime - 2, prime)
    fg = _fmt([a * b % prime * N_inv % prime for a, b in zip(Ff, Fg)], inverse = True)
    del fg[len(f) + len(g) - 1:]
    return fg

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

from collections import Counter
def resolve():
    n = int(input())
    H = [int(input()) for _ in range(2 * n)]

    mf = modfact(2 * n)
    doublefact = [1] * (2 * n + 2)
    for i in range(2, 2 * n + 1):
        doublefact[i] = i * doublefact[i - 2] % MOD

    F = [[mf.comb(k, 2 * i) * doublefact[2 * i - 1] % MOD for i in range(k // 2 + 1)] for k in Counter(H).values()]
    for i in range(len(F) - 1):
        F.append(convolution(F[2 * i], F[2 * i + 1]))

    f = F[-1]
    ans = sum(f[i] * doublefact[2 * (n - i) - 1] % MOD * (1 - 2 * (i & 1)) for i in range(len(f))) % MOD
    print(ans)
resolve()