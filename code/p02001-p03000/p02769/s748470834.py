MOD = 10**9 + 7
MOD_t_MAX = 2*(10**5)+1

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
def MOD_pow(a, n):
    res = 1
    while n > 0:
        if (n & 1):
            res = res * a % MOD
        a = a * a % MOD
        n = n // 2
    return res

def main():
    n, k = map(int, input().split())
    MOD_COM_init()
    ans = 0
    for i in range(n):
        if k-i < 0:
            continue
        x = MOD_COM(n, i) * MOD_COM(n-1, n-i-1) % MOD
        ans += x
        ans %= MOD
    print(ans)
if __name__ == "__main__":
    main()