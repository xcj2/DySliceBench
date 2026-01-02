#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

def gcd(a: int, b: int):
    while b:
        a, b = b, a%b
    return a

def lcm(a: int, b:int):
    return a*b // gcd(a,b)

def solve(A: int, B: int):
    print(lcm(A,B))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
