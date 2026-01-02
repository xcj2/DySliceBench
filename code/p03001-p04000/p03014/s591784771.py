#!/usr/bin/env python3
import sys


def solve(H: int, W: int, S: "List[str]"):
    c_h = [[0] * W for _ in range(H)]
    c_w = [[0] * W for _ in range(H)]
    for i in range(H):
        tmp = 0
        cnt = 0
        for j in range(W):
            if S[i][j] == '#':
                for k in range(tmp, j):
                    c_h[i][k] = cnt
                cnt = 0
                tmp = j + 1
            else:
                cnt += 1
        for k in range(tmp, W):
            c_h[i][k] = cnt
    for j in range(W):
        tmp = 0
        cnt = 0
        for i in range(H):
            if S[i][j] == '#':
                for k in range(tmp, i):
                    c_w[k][j] = cnt
                cnt = 0
                tmp = i + 1
            else:
                cnt += 1
        for k in range(tmp, H):
            c_w[k][j] = cnt
    ret = 0
    for i in range(H):
        for j in range(W):
            ret = max(ret, c_h[i][j] + c_w[i][j] - 1)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [ next(tokens) for _ in range(H) ]  # type: "List[str]"
    solve(H, W, S)

if __name__ == '__main__':
    main()
