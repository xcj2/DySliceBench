N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.sort()
MOD = 10 ** 9 + 7


def combination(mod=MOD):
    fact = [1] * (N + 1)
    inv_fact = [1] * (N + 1)
    r = 1
    for i in range(1, N + 1):
        fact[i] = r = r * i % mod
    inv_fact[N] = r = pow(fact[N], mod - 2, mod)
    for i in range(N, 0, -1):
        inv_fact[i - 1] = r = r * i % mod

    def _wrapper(n, k):
        nonlocal fact, inv_fact, mod
        if n == 0 or k == 0:
            return 1
        return fact[n] * inv_fact[k] * inv_fact[n - k] % mod

    return _wrapper


def main():
    if K == 1:
        print(0)
        exit()
    comb = combination()
    sum_max = 0
    sum_min = 0
    for i, A_i in enumerate(A):
        if i >= K - 1:
            sum_max += comb(i, K - 1) * A_i % MOD
        if N - i >= K:
            sum_min += comb(N - i - 1, K - 1) * A_i % MOD
    ans = (sum_max - sum_min) % MOD
    print(ans)


if __name__ == '__main__':
    main()
