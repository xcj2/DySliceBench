#!/usr/bin/env python3
import sys
import math
MOD = 1000000007  # type: int

def factorial(n):
    f = 1
    while n>0:
        f*=n
        f = f%MOD
        n-=1
    return f

def solve(X: int, Y: int):
    if X>2*Y or Y>2*X or (X+Y)%3!=0:
        print(0)
        return 
    
    N = (X+Y)//3 ##N階層め

    # N階層めの一番端のX
    left_x = 2*N
    r = left_x-X
    bunsi = factorial(N)
    bunbo = factorial(N-r)*factorial(r)
    bunbop = pow(bunbo,MOD-2,MOD)
    print(bunsi*bunbop%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(X, Y)

if __name__ == '__main__':
    main()
