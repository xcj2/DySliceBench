#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, A: "List[int]"):
    d = [[a > 0, abs(a)] for i, a in enumerate(A)]
    d.sort(key=lambda x: x[1], reverse=True)
    AA = [dv[1] if dv[0] else -dv[1] for dv in d]
    # print(AA)
    s = 0
    for i in range(N-1):
        if AA[i] < 0:
            AA[i] *= -1
            AA[i+1] *= -1
        s += AA[i]
    # print(AA)
    print(s+AA[-1])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
