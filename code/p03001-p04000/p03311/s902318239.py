#!/usr/bin/env python3
import sys

def calc(A, b):
    c = 0
    for i, x in enumerate(A):
        c += abs(x - (b + (i+1)))
    return c

def solve(N, A):
    B = []
    for i, a in enumerate(A):
        B.append(a - (i+1))
    return calc(A, sorted(B)[N // 2])

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, A))

if __name__ == '__main__':
    main()
