#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, v: "List[int]"):
    v.sort()
    tmp = (v[0] + v[1]) / 2
    for i in range(2, N):
        tmp = (tmp + v[i]) / 2
    ret = tmp
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    v = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, v)

if __name__ == '__main__':
    main()
