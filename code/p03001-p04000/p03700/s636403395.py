#!/usr/bin/env python3
import sys
import math
INF = float("inf")


def solve(N: int, A: int, B: int, h: "List[int]"):
    tot = sum(h)

    def isOK(index):
        base = B*index
        sub = A-B
        counter = 0
        for hh in h:
            if hh > base:
                counter += int(math.ceil((hh-base)/sub))
            if index < counter:
                return False

        return index >= counter

    ng = -1
    ok = 2*tot//(N*B) + 1
    # print(ng, ok)

    while abs(ok - ng) > 1:
        mid = (ok + ng)//2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, h)


if __name__ == '__main__':
    main()
