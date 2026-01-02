#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def _cmb(N, mod):
    N1 = N + 1
    fact = [0] * N1
    inv = [0] * N1
    fact[0] = fact[1] = inv[0] = inv[1] = 1

    for i in range(2, N1):
        fact[i] = fact[i-1] * i % mod
        inv[i] = pow(fact[i], mod-2, mod)

    def cmb(a, b):
        return fact[a] * inv[b] * inv[a-b] % mod
    return cmb

def resolve():
    K = int(input())
    s = input()
    ls = len(s) - 1
    mod = 10**9+7

    cmb = _cmb(ls+K, mod)

    ans = 0
    for i in range(K+1):
        ans += cmb(ls+i, ls) * pow(25, i, mod) * pow(26, K - i, mod)
        ans %= mod
    print(ans)

if __name__ == "__main__":
    resolve()
