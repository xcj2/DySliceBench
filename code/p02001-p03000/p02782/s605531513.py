MOD = 10**9+7
fac = [1, 1]
f_inv = [1, 1]
inv = [0, 1]

def prepare(n, mod):
    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod//i)) % mod)
        f_inv.append((f_inv[-1] * inv[-1]) % mod)


def modcmb(n, r, mod):
    if n < 0 or r < 0 or r > n:
        return 0

    return fac[n] * f_inv[r] * f_inv[n-r] % mod


def f(r, c):
    return modcmb(r+c, r, MOD)


def main():
    prepare(2*10**6+10, MOD)
    r1,c1,r2,c2 = map(int, input().split())

    ans = 0
    for i in range(1,c2+2):
        ans += f(r2, i)
        ans %= MOD

    for i in range(1,c2+2):
        ans -= f(r1-1, i)
        ans %= MOD

    for i in range(1,c1+1):
        ans -= f(r2, i)
        ans %= MOD

    for i in range(1,c1+1):
        ans += f(r1-1, i)
        ans %= MOD

    print(ans % MOD)


if __name__ == "__main__":
    main()
