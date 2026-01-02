#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, a: "List[int]"):
    s = 0
    for v in a:
        s = s ^ v
    ret = []
    for v in a:
        ret.append(s ^ v)
    print(*ret, sep=' ')
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
