#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, K: int, h: "List[int]"):
    ret = 0
    for i in range(N):
        if h[i] >= K:
            ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, h)

if __name__ == '__main__':
    main()
