#!/usr/bin/env python3
import sys


def solve(X: int):
    dp = [[-1]*(X+1) for _ in range(7)]
    price = [100,101,102,103,104,105]
    m = [10**5]*6

    for i in range(7):
        dp[i][0] = 10**5

    ## i番目まででjを払えるか
    for i in range(6):
        for j in range(X+1):
            if dp[i][j]>=0:
                dp[i+1][j] = m[i]
            elif j < price[i] or dp[i+1][j-price[i]]<=0:
                dp[i+1][j] = -1
            else:
                dp[i+1][j] = dp[i+1][j-price[i]]-1

    if dp[6][X]>=0:
        print(1)
    else:
        print(0)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()
