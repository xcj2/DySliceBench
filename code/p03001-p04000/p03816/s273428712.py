#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]"):
    s = set()
    for a in A:
        s.add(a)
    num = len(s)
    ret = num - (num + 1) % 2
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
