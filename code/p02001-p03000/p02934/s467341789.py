#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, A: "List[int]"):
    b = 1
    def mul(x: "List"):
        r = 1
        for i in x:
            r *= i

        return r
    
    u = 0
    for i in range(N):
        t = [A[j] for j in range(N) if j != i] 
        u += mul(t)

    print(mul(A)/u)
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
