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


def sum_rect(r, c, table):
    return (mod_combination(r+c+2, r+1, table)-1) % MOD


def main():
    r1, c1, r2, c2 = map(int, input().split())
    table = make_combination_table((r2+c2+2))
    r1 -= 1
    c1 -= 1

    ans = sum_rect(r2, c2, table)
    ans %= MOD
    ans -= sum_rect(r2, c1, table)
    ans %= MOD
    ans -= sum_rect(r1, c2, table)
    ans %= MOD
    ans += sum_rect(r1, c1, table)
    ans %= MOD
    print(ans)


main()
