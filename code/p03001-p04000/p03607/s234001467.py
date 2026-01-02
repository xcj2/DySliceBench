#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    s = set()
    for a in A:
        if a in s:
            s.remove(a)
        else:
            s.add(a)
    ret = len(s)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
