#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(X: int):
    dp = [False] * 110000
    
    dp[0] = True
    for i in range(100001):
        if dp[i]:
            for j in range(6):
                dp[i+100+j] = True

    print(1 if dp[X] else 0)
    

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
