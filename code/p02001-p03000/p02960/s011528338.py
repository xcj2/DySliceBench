#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


def solve(S: str):
    dp = [0]*13
    dp[0] = 1
    dpn = [0]*13
    keta = 1
    zero = 0
    # print(dp)
    for c in reversed(S):
        if c == "?":
            dpn = [0]*13
            for i in range(10):
                for j in range(13):
                    dpn[j] += dp[(j - i*keta) % 13]
                    dpn[j] %= MOD
            dp = dpn
        else:
            shift = (int(c)*keta) % 13
            dpn = [0]*13
            for i in range(13):
                dpn[i] = dp[(i-shift) % 13]
            # dpn = dp[13-shift:]+dp[:13-shift]
            dp = dpn

        # print(c, dp)
        keta *= 10
        keta %= 13

    print(dp[5])

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()
