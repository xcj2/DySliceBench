#!/usr/bin/env python3
import sys


def solve(N: int, V: "List[int]", C: "List[int]"):
    tmp = []
    for i in range(N):
        tmp.append(V[i] - C[i])
    tmp.sort(reverse=True)
    ret = 0
    for t in tmp:
        if t > 0:
            ret += t
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    V = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    C = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, V, C)

if __name__ == '__main__':
    main()
