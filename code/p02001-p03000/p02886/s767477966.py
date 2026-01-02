#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, d: "List[int]"):
    ret = 0
    for i in range(N):
        for j in range(i + 1, N):
            ret += d[i] * d[j]
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    d = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, d)

if __name__ == '__main__':
    main()
