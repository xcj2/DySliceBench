#!/usr/bin/env python3
import sys


def solve(N: int):
    dp = list(range(N + 1))
    for i in [6,9]:
        j = 1
        while i ** j <= N:
            base = i ** j
            idx = 0
            while idx + base <= N:
                dp[idx + base] = min(dp[idx + base], dp[idx] + 1)
                idx += 1
            j += 1
    #print(dp)
    ret = dp[N]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
