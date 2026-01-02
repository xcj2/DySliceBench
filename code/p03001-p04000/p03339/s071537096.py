#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    W = 0
    E = 0
    for c in S:
        if c == 'W':
            W += 1
        else:
            E += 1
    w, e = 0, 0
    ret = float('inf')
    for i in range(N):
        tmp = w + E - e
        if S[i] == 'W':
            w += 1
        else:
            e += 1
            tmp -= 1
        ret = min(ret, tmp)
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
