#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(H: int, W: int, S: "List[str]"):

    table1 = [[0]*W for _ in range(H)]
    for h in range(H):
        for i, c in enumerate(S[h]):
            if c == "#":
                table1[h][i] = 0
            else:
                if i == 0:
                    table1[h][i] = 1
                else:
                    table1[h][i] = table1[h][i-1]+1
    # for h in range(H):
    #     print(table1[h])
    # print()
    for h in range(H):
        buf = 0
        for w in range(W-1, -1, -1):
            if table1[h][w] != 0:
                if buf == 0:
                    buf = table1[h][w]
                table1[h][w] = buf
            else:
                buf = 0
    # for h in range(H):
    #     print(table1[h])
    table2 = [[0]*W for _ in range(H)]
    for w in range(W):
        for h in range(H):
            c = S[h][w]
            if c == "#":
                table2[h][w] = 0
            else:
                if h == 0:
                    table2[h][w] = 1
                else:
                    table2[h][w] = table2[h-1][w]+1
    # for h in range(H):
    #     print(table2[h])
    for w in range(W):
        buf = 0
        for h in range(H-1, -1, -1):
            if table2[h][w] != 0:
                if buf == 0:
                    buf = table2[h][w]
                table2[h][w] = buf
            else:
                buf = 0
    # print()
    # for h in range(H):
        # print(table2[h])

    m = -INF
    for h in range(H):
        for w in range(W):
            buf = table1[h][w] + table2[h][w]
            if buf > m:
                m = buf
                # print(h, w)
    print(m-1)

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
