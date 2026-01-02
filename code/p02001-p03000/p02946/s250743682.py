#!/usr/bin/env python3
import sys
import numpy as np


def solve(K: int, X: int):
    result = set()
    point = X - K
    for start in range(1, K + 1):
        base = [i for i in range(start, start + K)]
        arr = np.array(base) + point
        for element in arr:
            result.add(element)

    result = sorted(result)
    result = map(str, result)
    result = " ".join(result)

    print(result)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(K, X)


if __name__ == "__main__":
    main()
