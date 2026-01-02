#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, X: "List[int]", L: "List[int]"):

    # 区間に変換する
    segs = [(x-l, x+l) for x, l in zip(X, L)]
    segs.sort(key=lambda x: x[1])  # 尻でソート

    last = -INF
    count = 0
    for i in range(N):
        if last <= segs[i][0]:
            last = segs[i][1]
            count += 1
    print(count)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    L = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        L[i] = int(next(tokens))
    solve(N, X, L)


if __name__ == '__main__':
    main()
