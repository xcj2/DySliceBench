from sys import stdin, setrecursionlimit


def initialize_cmb(m, mod):
    fac = [0] * m
    finv = [0] * m
    inv = [0] * m
    fac[0] = 1
    finv[0] = 1
    if m > 1:
        fac[1] = 1
        finv[1] = 1
        inv[1] = 1
        for i in range(2, m):
            fac[i] = fac[i-1] * i % mod
            inv[i] = mod - inv[mod % i] * (mod // i) % mod
            finv[i] = finv[i - 1] * inv[i] % mod
    return fac, finv


def cmb(n, k, mod, fac, finv):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


def main():
    input = stdin.buffer.readline
    n, m, k = map(int, input().split())
    mod = 998244353

    fac, finv = initialize_cmb(n + 10, mod)

    c = [0] * (n + 1)
    c[0] = m
    for i in range(n):
        c[i + 1] = c[i] * (m - 1) % mod

    ans = c[n - 1]

    for i in range(k):
        ans += c[n - i - 2] * cmb(n - 1, i + 1, mod, fac, finv)
        ans %= mod

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
