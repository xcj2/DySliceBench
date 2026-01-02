#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, A: "List[int]"):

    sumA = sum(A)
    sortA = sorted(A, reverse=True)

    thresh = sumA / (4*M)

    for a in range(M):

        if sortA[a] < thresh:
            print(NO)
            return
    print(YES)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
