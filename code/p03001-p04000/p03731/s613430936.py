#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, T: int, t: "List[int]"):
    ret = T * N
    tmp = 0
    for v in t:
        ret -= max(0, tmp - v)
        tmp = v + T
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    t = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, T, t)

if __name__ == '__main__':
    main()
