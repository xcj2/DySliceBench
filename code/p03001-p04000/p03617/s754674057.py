#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(Q: int, H: int, S: int, D: int, N: int):
    h1 = min(2*Q, H)
    h1 = min(h1*2, S)
    d1 = D

    ans = 0
    if 2*h1 < d1:
        print(N*h1)
    else:
        if N%2 == 0:
            print((N//2)*d1)
        else:
            print((N//2)*d1 + h1)
    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(Q, H, S, D, N)

if __name__ == '__main__':
    main()
