#!/usr/bin/env python3
import sys


def solve(N: int, p: "List[int]"):
    counts = 0
    idx = 0
    while idx < len(p):
        if p[idx] == idx + 1:
            counts += 1
            idx += 1
        idx += 1
    #print(counts)
    ret = counts
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, p)

if __name__ == '__main__':
    main()
