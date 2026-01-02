#!/usr/bin/env python3
import sys


def solve(N: int, P: int, S: str):

    if P == 2 or P == 5:
        tot = 0
        for i, c in enumerate(S):
            c = int(c)
            if c % P == 0:
                tot += i+1
        print(tot)
        return

    U = [0]*(N+1)
    a = 0
    beki = 1
    for i in range(N-1, -1, -1):
        a += beki*int(S[i])
        a %= P
        U[i] = a
        beki = (beki * 10) % P
    table = [0]*P
    tot = 0
    for i in range(N-1, -1, -1):
        tot += table[U[i]]
        table[U[i]] += 1
    tot += table[0]
    print(tot)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    S = str(next(tokens))  # type: int
    solve(N, P, S)


if __name__ == '__main__':
    main()
