#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, T: int, A: "List[int]"):
    mx = 0
    mn = float('inf')
    ret = 0
    for a in A:
        if a < mn:
            mn = a
        if a - mn > mx:
            mx = a - mn
            ret = 1
        elif a - mn == mx:
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
    T = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, T, A)

if __name__ == '__main__':
    main()
