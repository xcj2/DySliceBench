#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, K: int, Q: int, A: "List[int]"):

    a = [0] * N
    for i in range(len(A)):
       a[A[i]-1] += 1

    for i in range(len(a)):
        if K + a[i] > Q:
            print(YES)
        else:
            print(NO)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, K, Q, A)

if __name__ == '__main__':
    main()
