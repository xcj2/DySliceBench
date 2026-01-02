#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(ABCD: str):
    A, B, C, D = map(int, ABCD)
    for op1 in [1, -1]:
        for op2 in [1, -1]:
            for op3 in [1, -1]:
                if A+op1*B+op2*C+op3*D == 7:
                    op1 = "+" if op1 == 1 else "-"
                    op2 = "+" if op2 == 1 else "-"
                    op3 = "+" if op3 == 1 else "-"
                    print("{}{}{}{}{}{}{}=7".format(A, op1, B, op2, C, op3, D))
                    return
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    ABCD = str(next(tokens))  # type: int
    solve(ABCD)


if __name__ == '__main__':
    main()
