#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, x: int, a: "List[int]"):
    ret = 0
    for i in range(1, N):
        if a[i] + a[i - 1] > x:
            hoge = (a[i] + a[i - 1]) - x
            ret += hoge
            tmp = min(hoge, a[i])
            a[i] -= tmp
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, x, a)

if __name__ == '__main__':
    main()
