#!/usr/bin/env python3
import sys


def solve(n: int, p: "List[int]"):

    count = 0
    for i in range(n - 2):
        partial = p[i : i + 2 + 1]
        if min(partial) != partial[1] and max(partial) != partial[1]:
            count += 1
        else:
            pass

    print(count)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, p)


if __name__ == "__main__":
    main()
