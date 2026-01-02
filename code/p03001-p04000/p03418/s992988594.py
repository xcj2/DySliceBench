#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    ret = 0
    if K == 0:
        ret = N * N
    else:
        for k in range(K + 1, N + 1):
            tmp = N // k
            mod = N % k
            ret += tmp * (k - K)
            ret += max(0, mod - K + 1)
            #print(k, tmp, k - K, mod, ret)
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
