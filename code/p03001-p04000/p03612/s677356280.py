#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, p: "List[int]"):
    counter = 0
    i = 0
    while i < N:
        if i+1 == p[i]:
            if i+1 < N and i+2 == p[i+1]:
                counter += 1
                i += 2
                continue
            else:
                counter += 1
                i += 1
                continue
        else:
            i += 1
            continue
    print(counter)

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
