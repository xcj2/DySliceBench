MOD = 10**9 + 7
MOD_t_MAX = 2*10**6 + 10

fac  = [None] * MOD_t_MAX
finv = [None] * MOD_t_MAX
inv  = [None] * MOD_t_MAX
def MOD_COM_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MOD_t_MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
def MOD_COM(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

def main():
    k = int(input())
    s = input()
    n = len(s)
    MOD_COM_init()
    ans = 0
    a = 1
    b = pow(26, k, MOD)
    for i in range(k+1):
        ans += a * MOD_COM(i + n-1, n-1) * b % MOD
        a *= 25
        b *= inv[26]
        a %= MOD
        b %= MOD
    print(ans % MOD)

if __name__ == "__main__":
    main()