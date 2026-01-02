#!/usr/bin/env python3
import sys
INF = float("inf")


def GCD(a, b):
    if a == 0:
        return b
    else:
        return GCD(b % a, a)


def solve(A: int, B: int, C: int, D: int):
    U = B-A+1
    cdivnum = B//C - (A-1)//C
    ddivnum = B//D - (A-1)//D
    cd = C*D//GCD(C, D)
    cddivnum = B//cd - (A-1)//cd
    print(U-cdivnum-ddivnum+cddivnum)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(A, B, C, D)


if __name__ == '__main__':
    main()
