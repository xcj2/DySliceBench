#!/usr/bin/env python3
import sys

def solve(N: int, A: "List[int]"):
    minus_count = 0
    
    for i in range(N):
        if A[i] < 0:
            minus_count += 1

    if minus_count % 2 == 0:
        result = sum([abs(x) for x in A])
    else:
        min_A = 10000000
        min_idx = -1
        for i, x in enumerate(A):
            if abs(x) < min_A:
                min_A = abs(x)
                min_idx = i
        result = 0
        for i, x in enumerate(A):
            if i == min_idx:
                result += abs(x) * -1
            else:
                result += abs(x)
    print(result)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
