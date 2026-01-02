import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    # dp[i] - is True if i gram of sugar is obtainable
    A, B, C, D, E, F = read_ints()
    dp = [0]*(F+1)
    for i in range(1, F+1):
        dp[i] = dp[i-1]
        if i-C >= 0:
            dp[i] = max(dp[i], dp[i-C]+C)
        if i-D >= 0:
            dp[i] = max(dp[i], dp[i-D]+D)

    highest_ratio = [0, 100*A]

    for a in range(31):
        for b in range(31):
            water = 100*A*a+100*B*b
            if water < F:
                sugar_limit = min(E*water//100, F-water)
                sugar = dp[sugar_limit]
                if sugar*highest_ratio[1] > water*highest_ratio[0]:
                    highest_ratio = [sugar, water]
    return sum(highest_ratio), highest_ratio[0]


if __name__ == '__main__':
    print(*solve())
