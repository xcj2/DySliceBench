#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, K: int):
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    ret = 0
    if N <= K:
        ret = min(K - N, N)
    else:
        tmp = N % K
        ret = min(K - tmp, tmp)
    print(ret)
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
