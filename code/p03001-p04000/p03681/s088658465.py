#!/usr/bin/env python3
import sys
import math
MOD = 1000000007  # type: int


def solve(N: int, M: int):
    if abs(N-M) >= 2:
        print(0)
        return 
    
    ## Nの並び替えパターン
    N_number = math.factorial(N)%MOD
    M_number = math.factorial(M)%MOD

    if N == M:
        print((N_number*M_number*2)%MOD)
    else:
        print((N_number*M_number)%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()
