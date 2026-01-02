#!/usr/bin/env python3
import sys


def solve(N: int, K: int, S: str):
    ret = ''
    for i, c in enumerate(S):
        if i + 1 == K:
            ret += c.lower()
        else:
            ret += c
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, S)

if __name__ == '__main__':
    main()
