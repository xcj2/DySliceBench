def main():
    import sys
    input = sys.stdin.readline

    mod = 1000000007
    r1, c1, r2, c2 = map(int, input().split())

    # comb init
    nmax = 2 * 10 ** 6 + 5  # change here
    fac = [0] * (nmax + 1)
    finv = [0] * (nmax + 1)
    inv = [0] * (nmax + 1)
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, nmax):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

    def comb(n, r):
        if n < r:
            return 0
        else:
            return (fac[n] * ((finv[r] * finv[n - r]) % mod)) % mod

    def f(r, c):
        ret = 0
        for i in range(r+1):
            ret = (ret + comb(i+1+c, c))%mod
        return ret

    print((f(r2, c2) - f(r2, c1-1) - f(c2, r1-1) + f(r1-1, c1-1))%mod)


if __name__ == '__main__':
    main()
