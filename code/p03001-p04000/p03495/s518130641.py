#!/usr/bin/env python3
import sys
import collections

def solve(N: int, K: int, A: "List[int]"):
    r = 0

    c = collections.Counter(A).most_common()
    while K < len(c):
        _, cnt = c.pop()
        r+=cnt
    return r


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, K, A))

if __name__ == '__main__':
    main()
