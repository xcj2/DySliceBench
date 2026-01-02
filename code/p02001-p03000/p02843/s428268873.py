#!/usr/bin/env python3
import sys


def solve(X: int):
    dp = [False for _ in range(X+1)]
    dp[0] = True
    prices = [100,101,102,103,104,105]
    for i in range(1,X+1):
        for price in prices:
            if i >= price:
                if dp[i-price]:
                    dp[i] = dp[i-price]
                    break
    
    print(int(dp[X]))
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
