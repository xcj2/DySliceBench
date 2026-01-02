#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    answer = 0

    for i in range(N):
        if A[i]>=B[i]:
            A[i] -= B[i]
            answer += B[i]
            B[i] = 0
        else:
            B[i] -= A[i]
            answer += A[i]
            A[i] = 0

            if A[i+1]>=B[i]:
                answer += B[i]
                A[i+1]-=B[i]
            else:
                answer += A[i+1]
                A[i+1]=0
    print(answer)
        
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N + 1)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B)

if __name__ == '__main__':
    main()
