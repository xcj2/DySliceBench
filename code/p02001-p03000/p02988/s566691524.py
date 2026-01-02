#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(n: int, p: "List[int]"):

    counter = 0
    for i in range(n-2):
        if p[i] < p[i+1] < p[i+2]:
            counter += 1
        elif p[i+2] < p[i+1] < p[i]:
            counter += 1
    print(counter)
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


if __name__ == '__main__':
    main()
