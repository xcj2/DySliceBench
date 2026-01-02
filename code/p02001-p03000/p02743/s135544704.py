#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(a: int, b: int, c: int):
    from decimal import Decimal
    from math import sqrt
    a,b,c = Decimal(a), Decimal(b), Decimal(c)

    if a.sqrt() + b.sqrt() < c.sqrt():
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
