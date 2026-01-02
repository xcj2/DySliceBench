MOD = 10**9+7


def make_cmb_table(n):
    fact = [1]
    for i in range(1, n+1):
        fact.append(fact[i-1] * i % MOD)

    ifact = [0] * (n+1)
    ifact[n] = pow(fact[n], MOD-2, MOD)
    for i in range(n, 0, -1):
        ifact[i-1] = ifact[i] * i % MOD
    return (fact, ifact)


def cmb(n, r, table):
    if r > n:
        return 0
    return table[0][n] * table[1][n - r] * table[1][r] % MOD


def main():
    n, k = map(int, input().split())
    k = min(k, n-1)
    table = make_cmb_table(n)
    ans = 0
    for i in range(k+1):
        ans += cmb(n, i, table) * cmb((n-i-1)+i, i, table) % MOD
        ans %= MOD
    print(ans)


main()
