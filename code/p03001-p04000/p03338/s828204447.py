#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, S: str):

    m = -INF
    for i in range(1, N):          # S[:i]とS[i:]
        kind = 0
        for c in set(S[:i]):
            if S[i:].count(c) > 0:
                kind += 1
        if kind > m:
            m = kind
        # print(S[:i], S[i:], kind)
    print(m)
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
