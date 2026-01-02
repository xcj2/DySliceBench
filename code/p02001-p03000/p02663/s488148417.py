#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62



def solve(H: "List[int]", M: "List[int]", K: int):
    start = H[0] * 60 + M[0]
    end = H[1] * 60 + M[1]
    print(end - start - K)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = [int()] * (2)  # type: "List[int]"
    M = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        H[i] = int(next(tokens))
        M[i] = int(next(tokens))
    K = int(next(tokens))  # type: int
    solve(H, M, K)

if __name__ == '__main__':
    main()
