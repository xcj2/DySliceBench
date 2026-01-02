#!/usr/bin/env python3
import sys
from math import ceil

def solve(N: int):
    if N == 0:
        print(0)
        return 

    answer = ""
    while N != 0:
        syou = ceil(N/-2) 
        amari = N-syou*-2

        answer+= str(amari)
        N = syou
    
    print(answer[::-1])

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
