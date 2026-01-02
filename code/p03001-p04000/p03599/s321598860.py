#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(A: int, B: int, C: int, D: int, E: int, F: int):

    mwater = 0
    msugar = 0
    mnoudo = 0

    # ope1
    for i in range(-(-F//100)*A+1):
        # ope2
        for j in range(-(-F//100)*B + 1):
            water = 100*A*i+100*B*j
            if water > F:
                break
            # ope3
            for k in range(-(-water*E//100)//C + 1):
                if water+C*k > F:
                    break
                for l in range(-(-water*E//100)//D + 1):
                    sugar = C*k + D*l
                    if water + sugar > F:
                        break
                    if (water*E/100) < sugar:
                        break
                    if water+sugar == 0:
                        break
                    noudo = 100*sugar/(water+sugar)
                    # print(water, sugar, noudo)
                    if mnoudo <= noudo:
                        mnoudo = noudo
                        mwater = water
                        msugar = sugar
    print(mwater+msugar, msugar)
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
    E = int(next(tokens))  # type: int
    F = int(next(tokens))  # type: int
    solve(A, B, C, D, E, F)


if __name__ == '__main__':
    main()
