
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

    pow26 = [1] * (K + 1)
    pow25 = [1] * (K + 1)
    t1 = 1
    t2 = 1
    for i in range(K + 1):
        pow25[i] = t1
        pow26[i] = t2
        t1 *= 25
        t1 %= MOD
        t2 *= 26
        t2 %= MOD

    fac, finv = COMinit(N + K, MOD)
    v = 1
    ans = 0
    for i in range(K + 1):
        ans += pow25[i] * Combination(N-1+i, N-1) * pow26[K-i]
        ans %= MOD
    print(ans)

if __name__ == "__main__":
    resolve()
