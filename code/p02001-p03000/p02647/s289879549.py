#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62


def naive(N, K, A):
    X = list(A)
    for _ in range(K):
        start = [0] * N
        end = [0] * N
        for i, x in enumerate(X):
            start[(max(0, i - x))] += 1
            end[min(i + x, N - 1)] += 1
        current = 0
        end_flag = True
        for i in range(N):
            current += start[i]
            X[i] = current
            if X[i] != N:
                end_flag = False
            current -= end[i]
        if end_flag:
            return X
    #     if all(x == N for x in X):
    #     print(X,start,end)
    #         return
    return X


def solve(N: int, K: int, A: "List[int]"):
    V = naive(N, K, A)
    print(' '.join(map(str, V)))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == '__main__':
    main()
