import math


def inputIntList():
    return [int(s) for s in input().split()]


def inputInt():
    return int(input())


def main():
    N = inputInt()
    h = inputIntList()
    h.append(0)
    dp = [float("inf") for _ in range(N + 2)]
    dp[0] = 0
    for i in range(N - 1):
        if abs(h[i] - h[i + 1]) + dp[i] < dp[i + 1]:
            dp[i + 1] = abs(h[i] - h[i + 1]) + dp[i]

        if abs(h[i] - h[i + 2]) + dp[i] < dp[i + 2]:
            dp[i + 2] = abs(h[i] - h[i + 2]) + dp[i]

    return dp[N - 1]


if __name__ == "__main__":
    print(main())
