#!/usr/bin/env python3
import sys
from collections import Counter
MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]"):
    counter = Counter(A)

    if N%2==0:
        for value in counter.values():
            if value%2!=0:
                print(0)
                return 
        
        print(2**(N//2)%MOD)
    else:
        for key,value in counter.items():
            if (value%2!=0 and int(key)!=0) or (value%2==0 and int(key)==0):
                print(0)
                return 
        
        print(2**((N-1)//2)%MOD)

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
