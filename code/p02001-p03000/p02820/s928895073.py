import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**5)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N, K = geta(int)
    R, S, P = geta(int)
    T = gete()

    def winner(c):
        return (R, 0, 0) if c == "s" else (0, P, 0) if c == 'r' else (0, 0, S)

    def fn(s):
        n = len(s)
        ret = 0
        dp = [[0] * 3 for _ in range(n)]

        dp[0] = winner(s[0])
        for i in range(1, n):
            w = winner(s[i])
            for j in range(3):
                dp[i][j - 2] = max(dp[i - 1][j - 1], dp[i - 1][j]) + w[j - 2]

        return (max(dp[n - 1]))

    print(sum(fn(T[i::K]) for i in range(K)))


if __name__ == "__main__":
    main()