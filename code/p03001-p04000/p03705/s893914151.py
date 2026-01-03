#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, A: int, B: int):
    if A > B :
        print(0)
    
    elif N == 1 and A == B:
        print(1)
    
    elif N == 1 and A < B:
        print(0)

    else:
        ans = (B*(N-2)-A*(N-2)+1)
        print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)

if __name__ == '__main__':
    main()
