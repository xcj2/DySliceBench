#!/usr/bin/env python3
import sys
import math

def solve(N: int, T: "List[int]", A: "List[int]"):
    current = [T[0],A[0]]
    for i in range(1,N):
        t = T[i]
        a = A[i]
        if current[0]>t or current[1]>a:
            multi = max((current[0]+t-1)//t,(current[1]+a-1)//a)
            t = t*multi
            a = a*multi
        
        current[0]=t
        current[1]=a

    print(sum(current))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int()] * (N)  # type: "List[int]"
    A = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        T[i] = int(next(tokens))
        A[i] = int(next(tokens))
    solve(N, T, A)

if __name__ == '__main__':
    main()
