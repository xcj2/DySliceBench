#!/usr/bin/env python3
import sys


def solve(N: int, l: "List[int]", r: "List[int]"):
    ret = 0
    for i in range(N):
        ret += r[i] - l[i] + 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    l = [int()] * (N)  # type: "List[int]" 
    r = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, l, r)

if __name__ == '__main__':
    main()
