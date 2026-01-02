#!/usr/bin/env python3
import sys
INF = float("inf")
import numpy as np

MOD = 1000000007  # type: int


def solve(N: int, K: int, a: "List[List[int]]"):
    a = np.asarray(a, dtype=object)
    ans = np.identity(N, dtype=object)
    while K > 0:
        if K & 1:
            ans = np.mod(np.dot(ans, a), MOD)
        a = np.mod(np.dot(a, a), MOD)
        K >>= 1
    print(ans.sum() % MOD)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [[int(next(tokens)) for _ in range(N)]
         for _ in range(N)]  # type: "List[List[int]]"
    solve(N, K, a)


if __name__ == '__main__':
    main()
