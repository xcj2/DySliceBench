#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: int, x: "List[int]"):
    dp = [[0] * 2501 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for s in range(2500, -1, -1):
            for j in range(N):
                if dp[j][s] > 0:
                    dp[j + 1][s + x[i]] += dp[j][s]
    ret = 0
    for i in range(1, N + 1):
        for j in range(2501):
            if j % i == 0 and j // i == A:
                ret += dp[i][j]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    x = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A, x)

if __name__ == '__main__':
    main()
