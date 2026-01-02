
def resolve():
    MOD = 10 ** 9 + 7

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

    K = int(input())
    S = input()
    N = len(S)
    n25 = [1]
    n26 = [1]
    for _ in range(K+N-N):
        n25.append((n25[-1] * 25) % MOD)
        n26.append((n26[-1] * 26) % MOD)

    fac, finv = COMinit(N + K, MOD)
    v = 1
    ans = 0
    for i in range(K + 1):
        ans += pow(25, i, MOD) * Combination(N-1+i, N-1) * pow(26, K-i, MOD)
        ans %= MOD
    print(ans)

if __name__ == "__main__":
    resolve()
