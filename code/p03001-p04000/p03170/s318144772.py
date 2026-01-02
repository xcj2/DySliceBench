#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, K: int, a: "List[int]"):

    # 石k個で勝利するプレイヤー0 or 1
    dp = [1]*(K+1)
    dp[0] = 1
    for k in range(1, K+1):
        dp[k] = 1
        for i in range(N):
            if k-a[i] >= 0 and dp[k-a[i]] == 1:
                dp[k] = 0
    print("First" if dp[K] == 0 else "Second")

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)


if __name__ == '__main__':
    main()
