#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, a: "List[int]"):
    ret = float('inf')
    mn = min(a)
    mx = max(a)
    for v in range(mn, mx + 1):
        tmp = 0
        for x in a:
            tmp += (x - v) ** 2
        ret = min(ret, tmp)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
