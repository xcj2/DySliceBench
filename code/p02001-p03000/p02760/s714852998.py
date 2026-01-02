#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(A: "List[List[int]]", N: int, b: "List[int]"):

    flag = False
    # 横
    for i in range(3):
        if A[i][0] in b and A[i][1] in b and A[i][2] in b:
            flag = True
            break
    # 縦
    for i in range(3):
        if A[0][i] in b and A[1][i] in b and A[2][i] in b:
            flag = True
            break
    # ななめ
    if A[0][0] in b and A[1][1] in b and A[2][2] in b:
        flag = True
    if A[0][2] in b and A[1][1] in b and A[2][0] in b:
        flag = True

    if flag:
        yes()
    else:
        no()

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(3)]
         for _ in range(3)]  # type: "List[List[int]]"
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(A, N, b)


if __name__ == '__main__':
    main()
