def d_factorization(N, M):
    if M == 1:
        return 1

    def prime_factorization_power_list(n):
        i = 2
        table = {}
        while i**2 <= n:
            table[i] = 0
            while n % i == 0:
                table[i] += 1
                n //= i
            if table[i] == 0:
                table.pop(i)
            i += 1
        if n > 1:
            table[n] = 1
        return table

    MOD = 10**9 + 7
    prime_m = prime_factorization_power_list(M)
    b_max = max(prime_m.values())  # 素因数分解の指数の最大値
    # フェルマーの小定理による組合せの計算
    factorial = [1] * (b_max + N)  # (b_i + N - 1)!を計算するため。0!も入れておく
    for k in range(1, b_max + N - 1):
        factorial[k + 1] = (factorial[k] * (k + 1)) % MOD
    # k!のmod 10**9+7における逆元を計算
    fact_inv = [1] * (b_max + N)
    fact_inv[b_max + N - 1] = pow(factorial[b_max + N - 1], MOD - 2, MOD)
    for k in range(b_max + N - 1, 0, -1):
        fact_inv[k - 1] = (fact_inv[k] * k) % MOD

    def nCr(n, r, M):
        if n < 0 or r < 0 or n < r:
            return 0
        else:
            return (factorial[n] * fact_inv[r] * fact_inv[n - r]) % M

    ans = 1
    for b in prime_m.values():
        ans = (ans * nCr(b + N - 1, b, MOD)) % MOD

    return ans

N, M = [int(i) for i in input().split()]
print(d_factorization(N, M))