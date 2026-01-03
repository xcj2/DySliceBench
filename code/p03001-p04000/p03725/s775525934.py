#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
from collections import deque
INF = float("inf")

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]


def solve(H: int, W: int, K: int, A: "List[str]"):

    y, x = -1, -1
    for i in range(1, H-1):
        for j in range(1, W-1):
            if A[i][j] == "S":
                y, x = i, j
                break
        if y != -1:
            break

    outer = INF
    outplace = (-1, -1)
    reachable = [[INF]*W for _ in range(H)]
    q = deque([(y, x, 0)])
    while len(q) > 0:
        y, x, d = q.popleft()

        # 到達可能な箇所で外に最も近い場所を探す
        dist = min([y, H-1-y, x, W-1-x])
        if dist < outer:
            outer = dist
            outplace = (y, x)

        if d == K:
            continue
        for dy, dx in zip(DY, DX):
            if not (0 <= y+dy < H):
                continue
            elif not (0 <= x+dx < W):
                continue
            elif A[y+dy][x+dx] == "#":
                continue
            else:
                if d+1 < reachable[y+dy][x+dx]:
                    reachable[y+dy][x+dx] = d+1
                    q.append((y+dy, x+dx, d+1))

    ans = 1 - (-outer // K)
    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, K, A)


if __name__ == '__main__':
    main()
