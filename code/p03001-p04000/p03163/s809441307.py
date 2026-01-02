import math


def inputIntList():
    return [int(s) for s in input().split()]


def inputInt():
    return int(input())


def main():
    N, capacity = inputIntList()
    w = [0 for _ in range(N)]
    v = [0 for _ in range(N)]
    for i in range(N):
        w[i], v[i] = inputIntList()

    dp = [[0 for _ in range(capacity + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(capacity + 1):
            if j < w[i]:
                dp[i + 1][j] = dp[i][j]
            else:

                dp[i + 1][j] = max(dp[i][j - w[i]] + v[i], dp[i][j])
            # print(dp)

    return dp[N][capacity]


if __name__ == "__main__":
    print(main())
