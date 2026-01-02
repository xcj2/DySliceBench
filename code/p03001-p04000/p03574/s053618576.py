#!/usr/bin/env python3
import sys
INF = float("inf")

DX = [-1, 0, 1, -1, 1, -1, 0, 1]
DY = [-1, -1, -1, 0, 0, 1, 1, 1]


def solve(H: int, W: int, S: "List[str]"):
    S = [list(s) for s in S]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            counter = 0
            for dx, dy in zip(DX, DY):
                if i+dy < 0 or H <= i+dy:
                    continue
                if j+dx < 0 or W <= j+dx:
                    continue
                if S[i+dy][j+dx] == "#":
                    counter += 1
            S[i][j] = str(counter)

    print(*["".join(s) for s in S], sep="\n")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)


if __name__ == '__main__':
    main()
