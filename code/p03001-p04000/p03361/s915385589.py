#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(H: int, W: int, s: "List[str]"):
    n = [[0]*(W+2) for _ in range(H+2)]
    for i in range(H):
        for j in range(W):
            if s[i][j] == "#":
                n[i+1][j+1] = 1  # 外枠を作りつつ

    flag = True
    for i in range(1, H+1):
        for j in range(1, W+1):
            # print(i, j)
            if n[i][j] == 1 and n[i-1][j]+n[i+1][j]+n[i][j-1]+n[i][j+1] == 0:
                flag = False
                break
        if flag == False:
            break
    if flag == False:
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
    s = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, s)


if __name__ == '__main__':
    main()
