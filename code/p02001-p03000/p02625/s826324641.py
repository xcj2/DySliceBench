import sys
sys.setrecursionlimit(10**6)

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


def combination(n, r, table):
    if r > n:
        return 0
    return table[0][n] * table[1][n - r] * table[1][r] % MOD


def permutation(n, k, table):
    return table[0][n] * table[1][n - k] % MOD


def main(input, print):
    n, m = map(int, input().split())
    ans = 0
    table = make_cmb_table(10**6+5)
    for i in range(n+1):
        now = combination(n, i, table)
        now %= MOD
        now *= (-1) ** i
        now *= permutation(m, i, table)
        now %= MOD
        now *= permutation(m-i, n-i, table) ** 2
        now %= MOD
        ans += now
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main(sys.stdin.readline, print)
