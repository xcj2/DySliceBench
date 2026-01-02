#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    A.sort(reverse=True)
    a = 0
    b = 0
    for i, v in enumerate(A):
        if i % 2 == 0:
            a += v
        else:
            b += v
    ret = a - b
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
