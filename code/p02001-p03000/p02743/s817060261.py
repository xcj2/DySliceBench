#!/usr/bin/env python3
import sys
import math
from decimal import *

YES = "Yes" 
NO = "No"  

def solve(a: int, b: int, c: int):
    if a + b + (2 * Decimal(a * b).sqrt()) - c < 0:
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
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    solve(a, b, c)

if __name__ == '__main__':
    main()
