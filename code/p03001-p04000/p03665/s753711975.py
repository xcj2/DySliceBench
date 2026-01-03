#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 2  # type: int

def solve(N: int, P: int, A: "List[int]"):

    if all([i%2 == 0 for i in A]):
        if P == 0:
            print(2**N)
        else:
            print(0)

    else:
        od = len([i%2 == 1 for i in A])
        print(2**(N-1))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, A)

if __name__ == '__main__':
    main()
