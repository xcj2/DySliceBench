#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def f(A, B, C, D, S):
    T = list(S)
    T[A] = "A"
    T[B] = "B"
    T[C] = "C"
    T[D] = "D"
    print("".join(T))


def solve(N: int, A: int, B: int, C: int, D: int, S: str):
    A = A-1
    B = B-1
    C = C-1
    D = D-1
    # f(A, B, C, D, S)

    def reachable(A, C, S):     # O(N)
        if A > C:
            return False
        # AからCへ到達可能ですか
        if S[A:C+1].find("##") == -1:
            return True
        else:
            return False

    if C > D:
        # できるだけ早く追い越す
        # 追い越すためには、"..."という領域が必要。
        oikoshi = S[B-1:].find("...")
        if oikoshi == -1:
            no()
            return
        if reachable(A, B-1+oikoshi, S) and reachable(B, B-1+oikoshi+1, S):
            A = B-1+oikoshi + 2
            B = B-1+oikoshi + 1
            # f(A, B, C, D, S)
        else:
            no()
            return

    # ２連岩なければ通れる
    if reachable(A, C, S) and reachable(B, D, S):
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
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, A, B, C, D, S)


if __name__ == '__main__':
    main()
