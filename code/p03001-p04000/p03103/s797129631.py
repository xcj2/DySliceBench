#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    AB = [(a,b) for (a,b) in zip(A,B)]
    AB = sorted(AB, key=lambda ab: ab[0])
    val = 0
    for (a,b) in AB:
        if M == 0:
            break
        if M >= b:
            val += a * b
            M -= b
        else:
            val += a * M
            M = 0
    print(val)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]" 
    B = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
