from functools import lru_cache

MOD = 998244353


def solve_baka(n, m, k):
    print('params:', n, m, k)
    ans = 0
    for i in range(m**n):
        s = ''
        for j in range(n):
            s = str(i % m) + s
            i = i // m
        cnt = 0
        for j in range(n-1):
            if s[j] == s[j+1]:
                cnt += 1
        if cnt <= k:
            ans += 1
        print(s, cnt <= k)
    print('ans:', ans)
    return ans


@lru_cache(maxsize=None)
def modpow(n, m):
    ret = 1
    while m > 0:
        if m & 1:
            ret = ret * n % MOD
        n = n * n % MOD
        m >>= 1
    return ret


def solve(n, m, k):
    factorial = [1]
    for i in range(1, max(n+1, m+1)):
        factorial.append(i*factorial[i-1] % MOD)
    permutation = [1]
    for i in list(range(1, n))[::-1]:
        permutation.append(i * permutation[-1] % MOD)

    ans = 0
    for i in range(0, k+1):
        val = m * permutation[i] % MOD
        val = val * modpow(factorial[i], MOD-2) % MOD
        val = val * modpow(m-1, n-1-i) % MOD
        ans = (ans + val) % MOD
    return ans


def main():
    # for n in range(3, 7):
    #     for m in range(1, 5):
    #         for k in range(0, n):
    #             assert solve_baka(n, m, k) == solve(n, m, k)
    n, m, k = map(int, input().split())
    print(solve(n, m, k))


if __name__ == '__main__':
    main()
