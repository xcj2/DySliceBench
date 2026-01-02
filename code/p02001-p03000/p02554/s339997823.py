#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def cmb_mod(N, mod=10**9+7):
    N1 = N + 1
    g1 = [0] * N1
    g2 = [0] * N1
    inv = [0] * N1
    g1[0] = g1[1] = g2[0] = g2[1] = inv[1] = 1

    for i in range(2, N1):
        g1[i] = g1[i-1] * i % mod
        inv[i] = -inv[mod % i ] * (mod//i) % mod
        #inv[i] = pow(g1[i-1], mod-2, mod)
        g2[i] = g2[i-1] * inv[i] % mod

    def cmb(n, a):
        if a < 0 or a > n:
            return 0
        return g1[n] * g2[a] * g2[n-a] % mod
    return cmb

def resolve():
    mod = 10**9 + 7
    N = int(input())

    cmb = cmb_mod(N)

    ans = 0
    x8 = 1
    ans = pow(10, N, mod)
    for i in reversed(range(1, N+1)):
        tmp = 2 * cmb(N, i) * x8 % mod
        ans = (ans - tmp) % mod
        x8 = x8*8 % mod

    ans = (ans - x8) % mod

    print(ans)

if __name__ == "__main__":
    resolve()
