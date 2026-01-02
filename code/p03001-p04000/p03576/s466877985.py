#!/usr/bin/env python3
import sys
from itertools import product
INF = float("inf")


def solve(N: int, K: int, x: "List[int]", y: "List[int]"):
    sx = sorted(x)
    sy = sorted(y)
    m = INF

    for (i, x1), (j, y1) in product(enumerate(sx[:-K+1]), enumerate(sy[:-K+1])):
        # 始点を固定
        for x2 in sx[i+1:]:
            for y2 in sy[j+1:]:
                # 終点を固定
                counter = sum([1 for xx, yy in zip(x, y)
                               if (x1 <= xx <= x2) and (y1 <= yy <= y2)])
                if counter >= K:
                    area = abs((y2-y1)*(x2-x1))
                    m = min(m, area)
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
