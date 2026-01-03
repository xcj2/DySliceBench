#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    ret = [0] * N
    for i in range(M):
        ret[a[i] - 1] += 1
        ret[b[i] - 1] += 1
    for r in ret:
        print(r)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]" 
    b = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)

if __name__ == '__main__':
    main()
