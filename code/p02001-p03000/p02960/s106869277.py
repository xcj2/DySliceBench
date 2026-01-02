#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)

# Override `input` function because `stdin.readline()` is 10x faster than built-in `input()`
input = sys.stdin.readline


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def main():
    S, = read_h(typ=str)
    n = len(S)

    MOD = 10**9 + 7

    dp = [[0] * 13 for _ in range(10**5 + 2)]
    dp[0][0] = 1
    #  print('initial dp:', dp)

    for i, s in enumerate(S):
        c = -1 if s == '?' else ord(s) - ord('0')
        #  print('c:', c)

        for j in range(10):
            if c != -1 and c != j:
                continue

            for k in range(13):
                dp[i + 1][(k * 10 + j) % 13] += dp[i][k]

            #  print('updated dp:', dp[:])

        for j in range(13):
            dp[i + 1][j] %= MOD

        #  print('final dp:', dp[:])

    res = dp[n][5]
    print(res)


if __name__ == '__main__':
    main()
