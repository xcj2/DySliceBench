#!/usr/bin/env python3
import sys

FIRST = "first"
SECOND = "second"

def solve(N: int, a: "List[int]"):
    for i in range(N):
        if a[i]%2 == 1:
            print(FIRST)
            return
    print(SECOND)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
