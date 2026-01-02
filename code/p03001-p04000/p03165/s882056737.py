import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    s = gete()
    t = gete()
    ans = ""

    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i, si in enumerate(s):
        for j, tj in enumerate(t):
            if si == tj:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    i, j = len(s), len(t)

    ans_r = ""
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            ans_r += s[i - 1]
            i -= 1
            j -= 1
        elif dp[i - 1][j] == dp[i][j]:
            i -= 1
        else:
            j -= 1

    print(ans_r[::-1])


if __name__ == "__main__":
    main()