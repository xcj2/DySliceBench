#!/usr/bin/env python3
import sys
from itertools import accumulate
from collections import Counter
from math import factorial
def nCr(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))

def solve(N: int, M: int, A: "List[int]"):
    a = list(accumulate(A))
    a = [aa%M for aa in a]
    counter = Counter(a)
    answer = a.count(0)

    for value in counter.values():
        if value <= 1:
            continue
        else:
            answer += nCr(value,2)
    
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
