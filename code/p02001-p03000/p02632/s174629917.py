#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def _cmb(N, mod):
    N1 = N + 1
    fact = [1] * N1
    inv = [1] * N1

    for i in range(2, N1):
        fact[i] = fact[i-1] * i % mod

    inv[N] = pow(fact[N], mod-2, mod)
    for i in range(N-1, 1, -1):
        inv[i] = inv[i+1]*(i+1) % mod

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
    p25 = 1
    p26 = pow(26, K, mod)
    p26inv = pow(26,  mod-2, mod)
    for i in range(K+1):
        ans += cmb(ls+i, ls) * p25 * p26
        ans %= mod
        p25 = p25 * 25 % mod
        p26 = p26 * p26inv % mod
    print(ans)

if __name__ == "__main__":
    resolve()
