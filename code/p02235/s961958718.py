from collections import defaultdict


def longest_common_subsequence(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[-1][-1]


def longest_common_subsequence2(s, t):
    dp = [0] * (len(t) + 1)
    for i in range(len(s)):
        si = s[i]
        tmp = dp[:]
        for j in range(len(t)):
            if si == t[j]:
                dp[j + 1] = tmp[j] + 1
            elif dp[j + 1] < dp[j]:
                dp[j + 1] = dp[j]
    return dp[-1]


def main():
    n = int(input())
    for _ in range(n):
        X, Y = input(), input()
        print(longest_common_subsequence2(X, Y))


if __name__ == '__main__':
    main()