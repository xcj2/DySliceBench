#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, T: "List[int]"):
    from functools import reduce

    def lcm_base(a: int, b:int):
        return a*b // gcd(a,b)

    def lcm(*numbers):
        return reduce(lcm_base, numbers, 1)

    def gcd_base(a: int, b: int):
        while b:
            a, b = b, a%b

        return a

    def gcd(*numbers):
        return reduce(gcd_base, numbers)

    print(lcm(*T))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T)

if __name__ == '__main__':
    main()
