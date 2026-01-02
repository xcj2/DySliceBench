#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(T: "List[int]", A: "List[int]", B: "List[int]"):

    if A[0] < B[0]:
        A, B = B, A

    if A[1] > B[1]:
        print(0)
        return
    elif A[0]*T[0]+A[1]*T[1] > B[0]*T[0]+B[1]*T[1]:
        print(0)
        return
    elif A[0]*T[0]+A[1]*T[1] == B[0]*T[0]+B[1]*T[1]:
        print("infinity")
        return

    K = (B[0]*T[0]+B[1]*T[1])-(A[0]*T[0]+A[1]*T[1])
    L = (A[0]-B[0])*T[0] // K
    if (B[0]-A[0])*T[0] % K == 0:
        print(2*L)
    else:
        print(2*L+1)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    A = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    solve(T, A, B)


if __name__ == '__main__':
    main()
