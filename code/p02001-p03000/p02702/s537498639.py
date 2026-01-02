#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(S: str):
    N = len(S)
    U = [0]*(N+1)
    a = 0
    beki = 1
    for i in range(N-1, -1, -1):
        a += beki*(ord(S[i])-ord("0"))
        a %= 2019
        beki = (beki*10) % 2019
        U[i] = a
    table = [0]*2019

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
    S = str(next(tokens))  # type: str
    solve(S)


if __name__ == '__main__':
    main()
