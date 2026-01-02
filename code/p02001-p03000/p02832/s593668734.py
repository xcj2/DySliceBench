#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, a: "List[int]"):
    target = 1
    ret = 0
    for v in a:
        if v != target:
            ret += 1
        else:
            target += 1
    if target == 1:
        ret = -1
    print(ret)
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
