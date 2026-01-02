#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int
import math
from itertools import accumulate

def mod_factorial(n):
    value = 1
    for i in range(n,0,-1):
        value*=i
        value%=MOD

    return value

def solve(N: int, x: "List[int]"):
    dif_x = []

    # factmod[i] = (N-1)!/iをMODで割ったあまり
    factmod = [0]*(N)
    factmod[1] = mod_factorial(N-1)
    for i in range(1,N):
        dif_x.append(x[i]-x[i-1])
    
    for i in range(2,N):
        factmod[i] = factmod[1]*pow(i,MOD-2,MOD)
    
    accum_fact_mod = list(accumulate(factmod))
        
    answer = 0

    for i in range(N-1):
        answer += accum_fact_mod[i+1]*dif_x[i]
        answer %= MOD
    
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, x)

if __name__ == '__main__':
    main()
