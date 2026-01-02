#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    dp = [[0,0] for _ in range(N+1)]
    dp[2] = [A[0],A[1]]
    
    for i in range(2,N):
        if (i+1)%2 ==0:
            dp[i+1][0] = dp[i-1][0]+A[i-1]
        else:
            dp[i+1][0] = max(dp[i])

        dp[i+1][1] = max(dp[i-1])+A[i]

    print(max(dp[N]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
