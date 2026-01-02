#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    count = 0
    for i in range(N):
        if A[i] < B[i]:
            count += A[i]
            diff = B[i] - A[i]
            count += min(A[i+1], diff)
            A[i+1] = max(0, A[i+1] - diff)
        else:
            count += B[i]
    print(count)        
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N+1) ]  # type: "List[int]"
    B = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A, B)

if __name__ == '__main__':
    main()
