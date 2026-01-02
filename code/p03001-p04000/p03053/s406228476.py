#!/usr/bin/env python3
import sys
from collections import deque
INF = float("inf")


def solve(H: int, W: int, A: "List[str]"):
    # 黒の位置をx, y座標として持つ。黒からの距離も一緒に持つ
    black = []
    B = [[-1]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if A[i][j] == "#":
                black.append((i, j, 0))
                B[i][j] = 0

    q = deque()
    q.extend(black)

    while len(q) > 0:
        cy, cx, dis = q.popleft()
        for y, x in zip([cy-1, cy, cy+1, cy], [cx, cx-1, cx, cx+1]):
            if 0 <= y < H and 0 <= x < W and B[y][x] < 0:
                B[y][x] = dis+1
                q.append((y, x, dis+1))

    m = -INF
    for i in range(H):
        a = max(B[i])
        if m < a:
            m = a
    print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, A)


if __name__ == '__main__':
    main()
