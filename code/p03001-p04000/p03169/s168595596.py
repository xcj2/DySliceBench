#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):

    c = [0]*4
    for A in a:
        c[A] += 1

    J = min(c[2]+c[3]+1, N+1)
    I = min(c[1]+c[2]+c[3]+1, N+1)
    kitai = [[[0]*(I+1) for _ in range(J+1)]
             for _ in range(c[3]+1)]
    for k in range(c[3]+1):
        for j in range(J):
            for i in range(I):
                tot = i+j+k
                if tot == 0 or tot > N:
                    continue
                res = N + kitai[k][j][i-1]*i + \
                    kitai[k][j-1][i+1]*j + kitai[k-1][j+1][i]*k
                kitai[k][j][i] = res/tot
    print(kitai[c[3]][c[2]][c[1]])

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
