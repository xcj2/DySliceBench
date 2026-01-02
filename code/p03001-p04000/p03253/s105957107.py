MOD = 10**9 + 7
m = 10**5 + 100
fac = [0] * m
finv = [0] * m
inv = [0] * m


def COMBinitialize(m):
    fac[0] = 1
    finv[0] = 1
    if m > 1:
        fac[1] = 1
        finv[1] = 1
        inv[1] = 1
        for i in range(2, m):
            fac[i] = fac[i-1] * i % MOD
            inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
            finv[i] = finv[i - 1] * inv[i] % MOD


def COMB(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


COMBinitialize(m)


def main():
    K, M = (int(i) for i in input().split())

    def prime_factorize(n):
        res = []
        for i in range(2, n+1):
            if i*i > n:
                break
            if n % i != 0:
                continue
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            res.append((i, ex))
        if n != 1:
            res.append((n, 1))
        return res

    pf = prime_factorize(M)

    ans = 1

    for _, n in pf:
        ans *= COMB(n+K-1, n)
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
