#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, A: "List[int]"):
    ans = 1
    t = 1
    for i in range(N):
        t *= 3
        if A[i]%2 == 0:
            ans *= 2
        
    print(t-ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
