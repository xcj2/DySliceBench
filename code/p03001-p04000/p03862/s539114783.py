#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, x: int, a: "List[int]"):
    ans = sum(a)

    if a[0] > x:
        a[0] = x

    for i in range(N-1):
        if a[i]+a[i+1] > x:
            a[i+1] -= (a[i]+a[i+1]-x)

    print(ans-sum(a))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, x, a)

if __name__ == '__main__':
    main()
