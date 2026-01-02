#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    ret = 0
    for i in range(1, N):
        l = set(S[:i])
        r = set(S[i:])
        count = 0
        for c in l:
            if c in r:
                count += 1
        ret = max(ret, count)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
