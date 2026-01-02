#!/usr/bin/env python3
import sys
import numpy as np
import math

def solve(N: int, K: int, A: "List[int]"):
    index_1 = np.argsort(A)[0]
    if K >= N:
        return print(1)
    l = index_1
    r = N - index_1 - 1
    ans = math.ceil((l + r) / (K - 1))
    print(ans)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
