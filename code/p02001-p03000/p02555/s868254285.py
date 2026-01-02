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
    S = int(input())

    if S < 3:
        print(0)
        return
    elif S < 6:
        print(1)
        return

    cmb = cmb_mod(S - 3 * 2 + 3)

    ans = 1
    for i in range(2, S//3+1):
        n = S - 3 * i + i - 1
        tmp = cmb(n, i - 1)
        ans = (ans + tmp) % mod
    print(ans)


if __name__ == "__main__":
    resolve()
