#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: int, B: int, C: int):
    if A+B > C:
        print(B+C)
    elif A+B == C:
        print(A+2*B)
    else:
        print(A+2*B+1)
        
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)

if __name__ == '__main__':
    main()
