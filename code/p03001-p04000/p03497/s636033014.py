#!/usr/bin/env python3
import sys
import collections


def solve(N: int, K: int, A):
    c = collections.Counter(A).most_common()
    z = 0
    m = len(c)
    for i in range(m - K):
        z += c[m - i -1][1]
    print(z)


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
