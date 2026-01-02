#!/usr/bin/env python3
import sys


def solve(N: int, x: "List[int]", y: "List[int]", h: "List[int]"):
    for cx in range(0,101):
        for cy in range(0,101):
            H= 0
            for i in range(N):
                if h[i] != 0:
                    H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
            for i in range(N):
                if max(H - abs(x[i]-cx) - abs(y[i]-cy),0) != h[i]:
                        break
                else:
                    continue
            else:
                print(cx,cy,H)
                return

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    h = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        h[i] = int(next(tokens))
    solve(N, x, y, h)

if __name__ == '__main__':
    main()
