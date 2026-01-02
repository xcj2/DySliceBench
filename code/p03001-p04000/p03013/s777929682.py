import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7
MIN = 100


def org(N, M, dp):
    a = [0] * M

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, max(N+1, MIN)):
        dp[i] = dp[i-1] + dp[i-2]

    ans = 1

    for i in range(M):
        a[i] = int(input())

        if i != 0 and abs(a[i] - a[i-1]) == 1:
            print(0)
            return

        if a[i] == 1:
            ans *= 1
        elif i == 0:
            ans *= dp[a[i] - 1]
            ans %= MOD
            # print(a[i], ans, a[i] - 1)
        else:
            ans *= dp[a[i] - a[i-1] - 2]
            ans %= MOD
            # print(a[i], ans, a[i] - a[i-1] - 2)

    if M == 0:
        ans *= dp[N]
        ans %= MOD
        # print(ans, N - a[M-1] - 1)
        print(ans)
    else:
        ans *= dp[N - a[M-1] - 1]
        ans %= MOD
        # print(ans, N - a[M-1] - 1)
        print(ans)


def good(N, M, dp):
    a = [0] * len(dp)

    for i in range(M):
        a[int(input())-1] = True

    dp[0] = 0 if a[0] is True else 1
    dp[1] = 0 if a[1] is True else dp[0] + 1

    if N == 1:
        print(dp[0])
        return
    elif N == 2:
        print(dp[1])
        return

    for i in range(2, N):
        if a[i] is True:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= MOD

    print(dp[N-1] % MOD)
    # print(dp)


def main():
    N, M = map(int, input().split())
    dp = [0] * max((N + 1), MIN)

    good(N, M, dp)


if __name__ == '__main__':
    main()
