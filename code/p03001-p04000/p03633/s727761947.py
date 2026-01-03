#!/usr/bin/env python3
import sys


def solve(N: int, T: "List[int]"):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    ret = T[0]
    for t in T:
        g = gcd(ret, t)
        ret = ret * t // g

    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, T)

if __name__ == '__main__':
    main()
