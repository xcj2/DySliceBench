#!/usr/bin/env python3
import sys


def solve(N: int):

    result_set = set()
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                result = str(i) + str(j) + str(k)
                result_set.add(result)
    print(len(result_set))

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == "__main__":
    main()
