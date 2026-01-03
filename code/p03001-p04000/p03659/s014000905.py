#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    s = sum(a)
    ret = float('inf')
    tmp = 0
    for i in range(N - 1):
        tmp += a[i]
        ret = min(ret, abs(tmp - (s - tmp)))
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
