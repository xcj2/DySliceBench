#!/usr/bin/env python3
import sys
from collections import Counter
import heapq
INF = float("inf")


def solve(N: int, K: int, A: "List[int]"):
    counter = Counter(A)
    # print(counter)
    values = sorted(counter.values())
    # print(values)
    if len(values) < K:
        print(0)
    else:
        print(sum(values[:len(values)-K]))
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
