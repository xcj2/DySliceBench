#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int):
    max_abc= max(A,B,C)

    dif = 3*max_abc-A-B-C
    if dif%2 == 0:
        print(dif//2)
    else:
        print((3*(max_abc+1)-A-B-C)//2)
    
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)

if __name__ == '__main__':
    main()
