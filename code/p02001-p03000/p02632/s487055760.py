
def resolve():
    def COMinit(n, MOD):
        fact = [1, 1]
        fact_inv = [1, 1]
        inv = [0, 1]
        for i in range(2, n + 1):
            fact.append((fact[-1] * i) % MOD)
            inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
            fact_inv.append((fact_inv[-1] * inv[i]) % MOD)
        return fact, fact_inv

    # 二項係数計算
    def Combination(n, k, MOD=10 ** 9 + 7):
        # fac, finv = COMinit(n, MOD)
        if n < k: return 0
        if n < 0 or k < 0: return 0
        ret = fac[n] * (finv[k] * finv[n - k] % MOD) % MOD
        return ret

    MOD = 10 ** 9 + 7
    K = int(input())
    S = input()
    N = len(S)

    fac, finv = COMinit(N + K, MOD)
    pow25 = 1
    pow26 = pow(26, K, MOD)
    inv26 = pow(26, MOD - 2, MOD)
    ans = 0
    for i in range(K + 1):
        ans += pow25 * Combination(N - 1 + i, N - 1) * pow26
        ans %= MOD
        pow25 = pow25 * 25 % MOD
        pow26 = pow26 * inv26 % MOD

    print(ans)

if __name__ == "__main__":
    resolve()
