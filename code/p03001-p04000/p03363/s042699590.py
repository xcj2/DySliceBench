#!/usr/bin/env python3
import sys
from itertools import accumulate
from collections import Counter
from math import factorial
def combinations_count(n, r):
    if n<r:
        return 0
    return factorial(n) // (factorial(n - r) * factorial(r))

def solve(N: int, A: "List[int]"):
    accum = accumulate(A)
    counter = dict(Counter(accum))

    answer = 0
    for key,value in counter.items():
        if key == 0:
            answer += value + combinations_count(value,2)
        else:
            answer += combinations_count(value,2)
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
