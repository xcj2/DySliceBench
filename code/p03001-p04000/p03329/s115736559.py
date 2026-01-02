#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int):
    cand = [1]
    a = 6
    while a < 10**5:
        cand.append(a)
        a *= 6
    a = 9
    while a < 10**5:
        cand.append(a)
        a *= 9
    cand.sort()
    M = len(cand)

    dp = [0]*(N+1)
    for i in range(1, N+1):
        dp[i] = min([dp[i-cand[j]]+1 for j in range(M) if i-cand[j] >= 0])
    print(dp[N])
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
