#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    switch_count = N if N%2 == 0 else N-1
    A.sort()
    sumA = sum(A)
    answer = sumA
    prev = sumA
    for i in range(2,switch_count+1,2):
        a = prev - A[i-1]*2 - A[i-2]*2
        answer = max(a,answer)
        prev = a
    print(answer)

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
