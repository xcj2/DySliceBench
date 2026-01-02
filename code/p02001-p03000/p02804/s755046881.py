MOD = 10**9+7


N = 10 ** 5+1  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)


def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % MOD


def solve(n, k, a):
    a.sort()
    sum_max = 0
    sum_min = 0

    for i in range(n):
        sum_max += cmb(i, k-1) * a[i]
        sum_min += cmb(n-1-i, k-1) * a[i]

    return (sum_max - sum_min) % MOD


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    result = solve(n, k, a)
    print(result)


if __name__ == "__main__":
    main()
