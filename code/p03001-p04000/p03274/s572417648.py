#!/usr/bin/env python3
import sys


def solve(N: int, K: int, x: "List[int]"):
    ret = float('inf')
    for i in range(K - 1, N):
        l = x[i - (K - 1)]
        r = x[i]
        if l < 0 and r > 0:
            tmp = min(abs(l) * 2 + r, abs(l) + r * 2)
            ret = min(ret, tmp)
        else:
            ret = min(ret, max(abs(r), abs(l)))
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
    x = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, x)

if __name__ == '__main__':
    main()
