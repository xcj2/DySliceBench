#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(n: int, a: "List[int]"):

    # 正スタート
    tot = 0
    countA = 0
    for i, x in enumerate(a):
        tot += x
        if i % 2 == 0:
            if tot <= 0:
                countA += -tot+1
                tot = 1
        else:
            if tot >= 0:
                countA += tot+1
                tot = -1

    tot = 0
    countB = 0
    for i, x in enumerate(a):
        tot += x
        if i % 2 == 1:
            if tot <= 0:
                countB += -tot+1
                tot = 1
        else:
            if tot >= 0:
                countB += tot+1
                tot = -1
    print(min(countA, countB))

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, a)


if __name__ == '__main__':
    main()
