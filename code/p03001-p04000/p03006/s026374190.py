#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, x: "List[int]", y: "List[int]"):
    if N == 1:
        print(1)
        return
    x, y = zip(*sorted(list(zip(x, y))))
    p_cand = [x[j]-x[i] for i in range(N) for j in range(i+1, N)]
    q_cand = [y[j]-y[i] for i in range(N) for j in range(i+1, N)]

    minimum = INF
    for p, q in set(zip(p_cand, q_cand)):
        # print("(p, q) = ({}, {})".format(p, q))
        xy = list(zip(x, y))
        cost = 0
        while len(xy) > 0:
            xx, yy = xy.pop()
            cost += 1
            # print(xx, yy, xy, xx-p, yy-q)
            while (xx-p, yy-q) in xy:
                xy.remove((xx-p, yy-q))
                xx -= p
                yy -= q
        if minimum > cost:
            minimum = cost
    print(minimum)

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
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)


if __name__ == '__main__':
    main()
