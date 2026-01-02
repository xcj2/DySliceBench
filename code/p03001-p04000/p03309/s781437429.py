#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    difA = [0]*N

    for i in range(N):
        difA[i] = A[i]-(i+1)

    difA.sort()
    if N%2 == 0:
        g1 = difA[N//2]
        g2 = difA[N//2-1]
        a1 = 0
        a2 = 0
        for i in range(N):
            a1 += abs(difA[i]-g1)
            a2 += abs(difA[i]-g2)
        print(min(a1,a2))
            
    else:
        g = difA[N//2]
        a = 0
        for i in range(N):
            a += abs(difA[i]-g)
        print(a)
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
