import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    # dp[i] - is True if i gram of sugar is obtainable
    A, B, C, D, E, F = read_ints()
    dp = [False]*(F+1)
    dp[0] = True
    for i in range(F+1):
        if i+C < F+1:
            dp[i+C] = dp[i+C] or dp[i]
        if i+D < F+1:
            dp[i+D] = dp[i+D] or dp[i]
    # dp2[i] - highest gram of sugars that is not greater than i
    dp2 = [0]*(F+1)
    highest_sugar = 0
    for i in range(F+1):
        if dp[i]:
            dp2[i] = highest_sugar = i
        else:
            dp2[i] = highest_sugar

    highest_ratio = [0, 100*A]

    for a in range(31):
        for b in range(31):
            water = 100*A*a+100*B*b
            if water < F:
                sugar_limit = min(E*water//100, F-water)
                sugar = dp2[sugar_limit]
                if sugar*highest_ratio[1] > water*highest_ratio[0]:
                    highest_ratio = [sugar, water]
    return sum(highest_ratio), highest_ratio[0]


if __name__ == '__main__':
    print(*solve())
