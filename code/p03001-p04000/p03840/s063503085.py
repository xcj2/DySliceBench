#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(a_I: int,
          a_O: int,
          a_T: int,
          a_J: int,
          a_L: int,
          a_S: int,
          a_Z: int):

    # O型は独立して考えて良い
    ans = a_O

    # I, J, L型の使い方はふた通り
    A = 2*(a_I//2) + 2*(a_J//2) + 2*(a_L//2)
    if a_I > 0 and a_J > 0 and a_L > 0:
        B = 3+2*((a_I-1)//2) + 2*((a_J-1)//2) + 2*((a_L-1)//2)
    else:
        B = 0
    ans += max(A, B)

    print(ans)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a_I = int(next(tokens))  # type: int
    a_O = int(next(tokens))  # type: int
    a_T = int(next(tokens))  # type: int
    a_J = int(next(tokens))  # type: int
    a_L = int(next(tokens))  # type: int
    a_S = int(next(tokens))  # type: int
    a_Z = int(next(tokens))  # type: int
    solve(a_I, a_O, a_T, a_J, a_L, a_S, a_Z)


if __name__ == '__main__':
    main()
