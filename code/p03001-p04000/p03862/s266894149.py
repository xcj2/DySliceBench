#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, x: int, a: "List[int]"):
    # 左から貪欲
    counter = 0
    for i in range(N-1):
        # i, i+1について
        if a[i] + a[i+1] <= x:
            continue
        if a[i] > x:
            counter += a[i] - x
            a[i] = x
            if a[i+1] != 0:
                counter += a[i+1]
                a[i+1] = 0
        else:
            counter += a[i]+a[i+1]-x
            a[i+1] = x-a[i]

    print(counter)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, x, a)


if __name__ == '__main__':
    main()
