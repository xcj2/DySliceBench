#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, M: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    # 全探索で間に合う
    for aa, bb in zip(a, b):
        m, mi = INF, -1
        for i, (cc, dd) in enumerate(zip(c, d)):
            dist = abs(aa-cc)+abs(bb-dd)
            if m > dist:
                m = dist
                mi = i
        print(mi+1)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    c = [int()] * (M)  # type: "List[int]"
    d = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, M, a, b, c, d)


if __name__ == '__main__':
    main()
