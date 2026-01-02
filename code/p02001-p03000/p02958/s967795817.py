#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(N: int, p: "List[int]"):
    count = 0

    for i, count_down in enumerate(range(1, N)):

        if not count_down == p[i]:
            count += 1

    if count <= 2:
        print(YES)
    else:
        print(NO)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, p)


if __name__ == '__main__':
    main()
