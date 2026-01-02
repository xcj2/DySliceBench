#!/usr/bin/env python3
import sys
import numpy as np


def solve(N: int, D: int, X: "List[List[int]]"):
    x_array = np.array(X)

    count = 0
    for i, x in enumerate(x_array):
        if not i == N:

            for x_target in x_array[i + 1 :]:

                distance = np.sqrt(np.power(x - x_target, 2).sum())
                if distance == int(distance):
                    count += 1
                else:
                    pass

        else:
            pss

    print(count)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    X = [
        [int(next(tokens)) for _ in range(D)] for _ in range(N)
    ]  # type: "List[List[int]]"
    solve(N, D, X)


if __name__ == "__main__":
    main()
