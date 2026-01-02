#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: "List[List[int]]", N: int, b: "List[int]"):
    for i in range(N):
        searchAndPut(A,b[i])

    # Horisonal
    if A[0][0] == A[0][1] == A[0][2] == -1:
            print(YES)
    elif A[1][0] == A[1][1] == A[1][2] == -1:
            print(YES)
    elif A[2][0] == A[2][1] == A[2][2] == -1:
            print(YES)
    # Vertical
    elif A[0][0] == A[1][0] == A[2][0] == -1:
            print(YES)
    elif A[0][1] == A[1][1] == A[2][1] == -1:
            print(YES)
    elif A[0][2] == A[1][2] == A[2][2] == -1:
            print(YES)
    # Cross
    elif A[0][0] == A[1][1] == A[2][2] == -1:
            print(YES)
    elif A[0][2] == A[1][1] == A[2][0] == -1:
            print(YES)
    else:
        print(NO)

def searchAndPut(A: "List[List[int]]",b):
    for i in range(3):
        list = A[i]
        if (b in list):
            list[list.index(b)] = -1
            break

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(A, N, b)

if __name__ == '__main__':
    main()
