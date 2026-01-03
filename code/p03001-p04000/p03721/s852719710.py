#!/usr/bin/env python3
import sys
import itertools

def solve(N: int, K: int, a: "List[int]", b: "List[int]"):
    ab = list(zip(a,b))
    ab.sort(key=lambda x: x[0])
    sumb =0
    123334
    for i in range(N):
        sumb+=ab[i][1]
        if sumb>=K:
            print(ab[i][0])
            return 
        
    

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, K, a, b)

if __name__ == '__main__':
    main()
