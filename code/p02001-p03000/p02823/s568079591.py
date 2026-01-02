#!/usr/bin/env python3
import sys


def solve(N: int, A: int, B: int):
    if (B-A)%2 == 0:
        between = (B-A)//2
        print(between)

    else: #端でしか会えない
        answer = 0
        if A-1<=N-B:
            answer += A
            B -= A
            A = 1
            answer += (B-A)//2
        else:
            answer += N-B+1
            A += N-B+1
            B = N
            answer += (B-A)//2

        print(answer)

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
