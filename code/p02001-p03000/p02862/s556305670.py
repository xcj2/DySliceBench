def factorial_mod(n, mod):
    a = 1
    for i in range(1, n + 1):
        a *= i
        a %= mod
    return a


def comb_mod(n, k, mod):
    if k > n or k < 0:
        return 0
    fact_n = factorial_mod(n, mod)
    fact_k = factorial_mod(k, mod)
    fact_n_k = factorial_mod(n - k, mod)
    return (fact_n * pow(fact_k, mod - 2, mod) * pow(fact_n_k, mod - 2, mod)) % mod


def main():
    x, y = map(int, input().split())
    MOD = 10 ** 9 + 7
    if (2 * x - y) % 3 != 0 or (2 * y - x) % 3 != 0:
        print(0)
        exit()
    i = (2 * x - y) // 3
    j = (2 * y - x) // 3
    print(comb_mod(i + j, i, MOD))


if __name__ == '__main__':
    main()
