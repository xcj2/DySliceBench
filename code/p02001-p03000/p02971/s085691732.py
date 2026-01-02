#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    left = [A[0]] * N
    right = [A[-1]] * N

    for i in range(1,N):
        left[i] = max(A[i], left[i-1])
    for i in reversed(range(0,N-1)):
        right[i] = max(A[i], right[i+1])

    for i in range(N):
        if i == 0:
            print(right[1])
        elif i == N-1:
            print(left[N-2])
        else:
            print(max(left[i-1], right[i+1]))


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
