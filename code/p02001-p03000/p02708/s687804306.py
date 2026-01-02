#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, K: int):
    res = 0
    r = 1000000007
    for k in range(K, N+2):
        # print(N-k+2, N+1, 1, k)
        res += (sigma(N-k+2, N+1) - sigma(1, k) + 1)
        res %= r

    print(res)


def sigma(left, right):
    return (right - left + 1) * (left + right) // 2


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
