from sys import stdin, setrecursionlimit


def main():
    mod = 10 ** 9 + 7
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    a.sort()
    ans = 0

    m = n + 1

    fac = [0] * m
    finv = [0] * m
    inv = [0] * m

    def initialize_cmb(m):
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

    def cmb(n, k, mod=10 ** 9 + 7):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return fac[n] * (finv[k] * finv[n - k] % mod) % mod

    initialize_cmb(m)

    for i in range(n - k + 1):
        ans -= a[i] * cmb(n - 1 - i, k - 1)
        ans %= mod
    for i in range(k - 1, n):
        ans += a[i] * cmb(i, k - 1)
        ans %= mod
    print(ans % mod)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()