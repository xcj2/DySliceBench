#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, a: "List[int]"):
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    g = a[0]
    for v in a:
        tmp = gcd(g, v)
        g = g * v // tmp
        if M < g // 2:
            print(0)
            return
    for v in a:
        if (g // v) % 2 == 0:
            print(0)
            return
    M -= g // 2
    ret = M // g + 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, a)

if __name__ == '__main__':
    main()
