#!/usr/bin/env python3
import sys


def solve(N: int, M: int, a: "List[int]"):
    a.sort(key=lambda x: x[1])
    ret = 1
    cur = a[0][1]
    for t in a:
        if t[0] >= cur:
            ret += 1
            cur = t[1]
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
    a = []
    for i in range(M):
        a.append((int(next(tokens)), int(next(tokens))))
    solve(N, M, a)

if __name__ == '__main__':
    main()
