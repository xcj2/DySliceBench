N, M = map(int, input().split())
MAX_N = 10 ** 5 + 2000
factors, MOD = {}, 10 ** 9 + 7
fact, fact_inv = [1] * (MAX_N+1), [1] * (MAX_N+1)


def prime_factorization(n):
    i = 2
    while i * i <= n:
        while not n % i:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1

    if n != 1:
        factors[n] = 1


def combination(n, r):
    return fact[n] * fact_inv[r] * fact_inv[n-r] % MOD


def main():
    prime_factorization(M)

    for i in range(1, N+2001):
        fact[i] = fact[i-1] * i % MOD

    fact_inv[N+2000] = pow(fact[N+2000], MOD-2, MOD)
    for i in range(N+1999, -1, -1):
        fact_inv[i] = fact_inv[i+1] * (i+1) % MOD

    ans = 1
    for i, j in factors.items():
        ans = ans * combination(j+N-1, j) % MOD

    print(ans)


if __name__ == '__main__':
    main()
