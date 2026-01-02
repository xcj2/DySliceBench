#!/usr/bin/env python3
import sys


def solve(N: int, H: "List[int]"):

    result = 0
    count = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            count += 1
        else:
            result = max(result, count)
            count = 0
    result = max(result, count)
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, H)


if __name__ == "__main__":
    main()
