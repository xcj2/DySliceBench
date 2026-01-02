import math

MOD = 10**9+7


def make_combination_table(n):
    fact = [1]
    for i in range(1, n+1):
        fact.append(fact[i-1] * i % MOD)

    ifact = [0] * (n+1)
    ifact[n] = pow(fact[n], MOD-2, MOD)
    for i in range(n, 0, -1):
        ifact[i-1] = ifact[i] * i % MOD
    return (fact, ifact)


def mod_combination(n, r, table):
    if r > n:
        return 0
    return table[0][n] * table[1][n - r] * table[1][r] % MOD


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    c_table = make_combination_table(n)

    a.sort()
    a_max = 0
    for i in range(n):
        a_max += a[i] * mod_combination(i, k-1, c_table) % MOD

    a.sort(reverse=True)
    a_min = 0
    for i in range(n):
        a_min += a[i] * mod_combination(i, k-1, c_table) % MOD

    print((a_max - a_min) % MOD)


main()
