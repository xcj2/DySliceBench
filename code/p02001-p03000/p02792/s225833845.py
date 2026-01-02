#!/usr/bin/env python3
import sys
import math
INF = float("inf")


def solve(N: int):
    table = [[0]*10 for _ in range(10)]

    for i in range(1, N+1):
        first = int(str(i)[0])
        last = int(str(i)[-1])
        table[first][last] += 1

    count = 0
    for i in range(10):
        for j in range(10):
            count += table[i][j]*table[j][i]
    print(count)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
