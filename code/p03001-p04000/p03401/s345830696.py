#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    dif = [0]*(N+1) 
    dif2 = [0]*N
    A = [0] + A + [0]
    for i in range(N+1):
        dif[i] = abs(A[i+1]-A[i])
    for i in range(N):
        dif2[i] = abs(A[i+2]-A[i])
    total_distance = sum(dif)
    
    # output answer
    for i in range(N):
        print(total_distance-dif[i]-dif[i+1]+dif2[i])

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
