# https://atcoder.jp/contests/agc043/tasks/agc043_a

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


ans = (100 * 100) + 1


def main():
    global ans
    h, w = input_int_list()
    grid = []
    grid.append(["#"] * (w + 2))
    for _ in range(h):
        grid.append(["#"] + list(input()) + ["#"])
    grid.append(["#"] * (w + 2))

    dp = [[101 for _ in range(w + 2)] for _ in range(h + 2)]
    if grid[1][1] == "#":
        dp[1][1] = 1
    else:
        dp[1][1] = 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            # 上のマスからくる場合を評価
            if i > 1:
                if grid[i - 1][j] == "." and grid[i][j] == "#":
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j])
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])

            # 左のマスからくる場合を評価
            if j > 1:
                if grid[i][j - 1] == "." and grid[i][j] == "#":
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i][j])
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i][j])

    print(dp[h][w])
    return


if __name__ == "__main__":
    main()
