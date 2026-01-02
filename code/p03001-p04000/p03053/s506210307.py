#!/usr/bin/env python3
import sys
from pprint import pprint

def solve(H: int, W: int, A: "List[str]"):
    used = [[False] * W for _ in range(H)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    s = set()
    for i in range(H):
        for j in range(W):
            if A[i][j] == '#':
                s.add((i, j))
                used[i][j] = True

    ret = 0
    while True:
        nex = set()
        for x, y in s:
            for j in range(4):
                tx = x + dx[j]
                ty = y + dy[j]
                if 0 <= tx < H and 0 <= ty < W and not used[tx][ty]:
                    nex.add((tx, ty))
                    used[tx][ty] = True
        if len(nex) < 1:
            break
        s = nex
        ret += 1

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
    A = [next(tokens) for _ in range(H) ]  # type: "List[str]"
    solve(H, W, A)

if __name__ == '__main__':
    main()
