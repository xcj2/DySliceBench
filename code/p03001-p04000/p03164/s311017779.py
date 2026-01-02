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

    dp = [[float("inf") for _ in range(N * 1000 + 1)] for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N * 1000 + 1):
            if j < v[i]:
                dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
            else:
                dp[i + 1][j] = min(dp[i][j - v[i]] + w[i], dp[i][j])
    ret = 0
    for value, weight in enumerate(dp[N]):
        if weight <= capacity:
            ret = max(ret, value)

    return ret


if __name__ == "__main__":
    print(main())
