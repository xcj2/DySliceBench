#!/usr/bin/env python3
import sys
import collections


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, K: int, Q: int, A: "List[int]"):
    cc = collections.Counter(A)
    for i in range(N):
        if Q - cc[i+1] < K:
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
