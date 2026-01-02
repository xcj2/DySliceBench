#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, K: int, x: "List[int]", y: "List[int]"):
    sx = sorted(x)
    sy = sorted(y)
    acc = [[0]*N for _ in range(N)]

    for i, x1 in enumerate(sx):
        for j, y1 in enumerate(sy):
            acc[i][j] = sum([True for xx, yy in zip(x, y)
                             if xx <= x1 and yy <= y1])

    m = INF

    for i, x1 in enumerate(sx[:-K+1]):
        for j, y1 in enumerate(sy[:-K+1]):
            # 始点を固定
            for x2 in sx[i+1:]:
                for y2 in sy[j+1:]:
                    # 終点を固定
                    counter = 0
                    for xx, yy in zip(x, y):
                        if (x1 <= xx <= x2) and (y1 <= yy <= y2):
                            counter += 1
                    if counter >= K:
                        flag = True
                        area = abs((y2-y1)*(x2-x1))
                        if area < m:
                            m = area
                        break   # これ以上yをあげたところで面積は増える一方なので抜ける
    print(m)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, K, x, y)


if __name__ == '__main__':
    main()
