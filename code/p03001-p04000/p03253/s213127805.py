import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9+7

fac = [1, 1]     # 元テーブル
f_inv = [1, 1]   # 逆元テーブル
inv = [0, 1]     # 逆元テーブル計算用テーブル
def prepare(n, mod):
    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)


def cmb(n, r, mod):
    if n < 0 or r < 0:
        return 0
    if r > n:
        return 0

    return fac[n] * pow(fac[r],MOD-2,MOD) * pow(fac[n-r],MOD-2,MOD) % mod


def prime_factorization(n):
    d = []
    i, e = 2, 0  # factor, exponent
    while i * i <= n:
        while n % i == 0:
            n //= i
            e += 1
        if e > 0:
            d.append((i, e))
        i += 1
        e = 0
    if n > 1:
        d.append((n, 1))
    return d


def main():
    N,M = map(int, readline().split())

    prepare(N+100, MOD)
    d = prime_factorization(M)

    ans = 1
    for i, e in d:
        ans *= cmb(N-1+e, e, MOD)
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
