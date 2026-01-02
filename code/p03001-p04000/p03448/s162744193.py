#!/usr/bin/env python3
from itertools import product
import sys
 
 
def solve(AA: int, BB: int, CC: int, XX: int):
    print(sum(
        1
        for a, b, c in product(range(AA + 1), range(BB + 1), range(CC + 1))
        if a * 500 + b * 100 + c * 50 == XX
    ))
 
 
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(A, B, C, X)
 
 
if __name__ == '__main__':
    main()