MAX = 10 ** 6
MOD = 10 ** 9 + 7
fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX


def COMinit():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def COM(n, r):
    if n < r or r < 0 or n < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD


def main():
    COMinit()
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)

    i = 0
    sum_max = 0
    sum_min = 0
    while n - i - 1 >= k - 1:
        cnt = COM(n - i - 1,  k - 1)
        sum_max += a[i] * cnt
        sum_min += a[n - i - 1] * cnt
        i += 1
    ans = (sum_max - sum_min) % MOD
    print(ans)


if __name__ == '__main__':
    main()