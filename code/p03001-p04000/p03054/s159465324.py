#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("YES")  # type: str


def no():
    print("NO")  # type: str


def solve(H: int, W: int, N: int, s_r: int, s_c: int, S: str, T: str):

    winner = "保留"

    cy, cx = s_r, s_c
    for i in range(N):
        # 高橋名人のR,D作戦
        if S[i] == "R":
            cx += 1
        elif S[i] == "D":
            cy += 1

        if H < cy or W < cx:
            winner = "TAKAHASHI"
            break

        # 青木名人のL,U作戦
        if T[i] == "L" and cx > 1:
            cx -= 1
        elif T[i] == "U" and cy > 1:
            cy -= 1

    if winner == "TAKAHASHI":
        no()
        return

    cy, cx = s_r, s_c
    for i in range(N):
        # 高橋名人のL,U作戦
        if S[i] == "L":
            cx -= 1
        elif S[i] == "U":
            cy -= 1

        if cy <= 0 or cx <= 0:
            winner = "TAKAHASHI"
            break

        # 青木名人のR, D作戦
        if T[i] == "R" and cx < W:
            cx += 1
        elif T[i] == "D" and cy < H:
            cy += 1

    if winner == "TAKAHASHI":
        no()
    else:
        yes()
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    s_r = int(next(tokens))  # type: int
    s_c = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(H, W, N, s_r, s_c, S, T)


if __name__ == '__main__':
    main()
