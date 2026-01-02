N, K = map(int, input().split())
A = [int(x) for x in input().split()]


def solve(N, K, A):
    A.sort()
    res = 0
    MOD = 10**9 + 7
    fact_table = [1] * (N + 1)
    inv_fact_table = [1] * (N + 1)
    for i in range(1, N + 1):
        fact_table[i] = fact_table[i - 1] * i % MOD

    def inverse(n):
        if n == 1:
            return 1
        q = MOD // n
        r = MOD % n
        return (MOD - q * inverse(r) % MOD) % MOD

    inv_fact_table[N] = inverse(fact_table[N])
    for i in range(N - 1, 0, -1):
        inv_fact_table[i] = inv_fact_table[i + 1] * (i + 1) % MOD

    def comb(n, k):
        return fact_table[n] * inv_fact_table[n - k] % MOD * inv_fact_table[k] % MOD

    s = [1, -1]
    for m in range(2):
        for i in range(K - 1, N):
            res = (res + s[m] * A[i] * comb(i, K - 1)) % MOD
        A = sorted(A, reverse=True)
    return (res + MOD) % MOD


print(solve(N, K, A))
