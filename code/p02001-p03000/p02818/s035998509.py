#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: int, B: int, K: int):
    t = max(0, A-K)
    a = B
    if A-K > 0:
        a = B
    else:
        a = max(0, a- (K-A))

    print(t, a)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(A, B, K)

if __name__ == '__main__':
    main()
