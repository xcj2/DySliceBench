import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9 + 7

fac = [1, 1]     # 元テーブル
f_inv = [1, 1]   # 逆元テーブル
inv = [0, 1]     # 逆元テーブル計算用テーブル
def prepare(n, mod):
    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod//i)) % mod)
        f_inv.append((f_inv[-1] * inv[-1]) % mod)


def cmb(n, r, mod):
    if n < 0 or r < 0:
        return 0
    if r > n:
        return 0

    return fac[n] * f_inv[r] * f_inv[n-r] % mod


def prime_factorization(n):
    d = {}
    i = 2
    while i * i <= n:
        if n % i == 0:
            d[i] = 1
            n //= i
            while n % i == 0:
                n //= i
                d[i] += 1
        i += 1
    if n > 1:
        d[n] = 1
    return d


def main():
    N,M = map(int, readline().split())

    prepare(N+100, MOD)
    d = prime_factorization(M)

    ans = 1
    for v in d.values():
        ans *= cmb(N-1+v, v, MOD)
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()
