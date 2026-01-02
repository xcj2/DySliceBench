import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    dp = [0] * (n + 1)  # dp[n] :: n円を引き出す最小の手数

    for i in range(1, n + 1):
        # 1円引き出す
        dp[i] = dp[i - 1] + 1
        # 6**n円引き出す
        j = 6
        while j <= i:
            dp[i] = min(dp[i], dp[i - j] + 1)
            j *= 6
        # 9**n円引き出す
        j = 9
        while j <= i:
            dp[i] = min(dp[i], dp[i - j] + 1)
            j *= 9
    print(dp[n])
    return


if __name__ == "__main__":
    main()
