def factorization(n):
    from collections import Counter
    arr = Counter()
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] = cnt

    if temp != 1:
        arr[temp] = 1

    if len(arr.keys()) == 0 and n != 1:
        arr[n] = 1

    return arr


def solve(m, N):
    MOD = 10 ** 9 + 7
    dp = [[0] * (m + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(m + 1):
            dp[i + 1][j] = dp[i + 1][j - 1] + dp[i][j]
            dp[i + 1][j] %= MOD
    return dp[-1][-1]


def main():
    # import sys
    # readline = sys.stdin.readline
    # readlines = sys.stdin.readlines
    MOD = 10 ** 9 + 7
    N, M = map(int, input().split())
    primes = factorization(M)

    ans = 1
    for p in primes.values():
        cnt = solve(p, N)
        ans *= cnt
        ans %= MOD
    
    print(ans)


if __name__ == "__main__":
    main()
