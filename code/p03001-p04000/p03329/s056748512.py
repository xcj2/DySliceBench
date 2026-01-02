import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    dp = [math.inf]*(N+1)
    dp[0] = 0
    for i in range(N):
        if i+1 <= N:
            dp[i+1] = min(dp[i+1], dp[i]+1)
            six = 6
            while i+six <= N:
                dp[i+six] = min(dp[i+six], dp[i]+1)
                six *= 6
            nine = 9
            while i+nine <= N:
                dp[i+nine] = min(dp[i+nine], dp[i]+1)
                nine *= 9
    return dp[N]


if __name__ == '__main__':
    print(solve())
