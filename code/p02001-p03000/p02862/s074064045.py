#!/usr/bin/env python3

MOD = 1000000007  # type: int


def comb(n, r):
    if (r < 0 or r > n):
        return 0
    r = min(r, n-r)
    g1 = [1] * (n + 1)
    g2 = [1] * (n + 1)
    ig = [0] * (n + 1)
    ig[1] = 1
    for i in range(2, n + 1):
        g1[i] = (g1[i-1] * i) % MOD
        ig[i] = (-ig[MOD % i] * (MOD//i)) % MOD
        g2[i] = (g2[i-1] * ig[i]) % MOD
    return g1[n] * g2[r] * g2[n-r] % MOD


def solve(X: int, Y: int):
    if (X + Y) % 3:
        return 0
    t = (X + Y) // 3
    return comb(t, X - t) % MOD


def main():
    X, Y = sorted(map(int, input().split()))
    print(solve(X, Y))


if __name__ == '__main__':
    main()
