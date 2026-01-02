#!/usr/bin/env python3
import sys
import math

MOD = 1000000007  # type: int
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def solve(N: int, K: int):
    for i in range(1,K+1):
        split_pattern = combinations_count(K-1,i-1)
        if N-K >= i-1:
            print((split_pattern*combinations_count(N-K+1,i))%MOD)
        else:
            print(0)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
