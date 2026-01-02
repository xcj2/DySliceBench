#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, B: "List[int]"):
    ret = 0
    for i in range(N - 2):
        ret += min(B[i], B[i + 1])
    ret += B[0] + B[N - 2]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    B = [ int(next(tokens)) for _ in range(N-1) ]  # type: "List[int]"
    solve(N, B)

if __name__ == '__main__':
    main()
