#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(N: int, M: int, A: "List[str]", B: "List[str]"):

    for i in range(N-M+1):
        for j in range(N-M+1):
            flag = True
            for k in range(M):
                for l in range(M):
                    if A[i+k][j+l] != B[k][l]:
                        flag = False
                        break
                if flag == False:
                    break
            if flag == True:
                yes()
                return

    no()
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(N)]  # type: "List[str]"
    B = [next(tokens) for _ in range(M)]  # type: "List[str]"
    solve(N, M, A, B)


if __name__ == '__main__':
    main()
