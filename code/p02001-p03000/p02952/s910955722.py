#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int):
    counter = 0
    for i in range(len(str(N))-1, 0, -1):
        if i % 2 == 0:
            continue
        counter += 9*(10**(i-1))
    if len(str(N)) % 2 == 1:
        counter += N-10**(len(str(N))-1)+1
    print(counter)

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
