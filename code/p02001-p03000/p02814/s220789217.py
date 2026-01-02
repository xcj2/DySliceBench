#!/usr/bin/env python3
import sys
from functools import reduce
import numpy as np
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, a: "List[int]"):

    def gcd_base(a: int, b: int):
        while b:
            a, b = b, a%b
        return a

    def gcd(*numbers):
        return reduce(gcd_base, numbers)
    
    def lcm_base(a: int, b:int):
        return a*b // gcd_base(a,b)

    def lcm(*numbers):
        return reduce(lcm_base, numbers, 1)

    def div_of_2(x: int):
        c = 0
        while x%2 == 0:
            c += 1
            x //= 2
        return c

    x = lcm(*a)
    t = x // 2
    y = div_of_2(x)

    if t > M or any([y != div_of_2(i) for i in a]):
        print(0)
        exit()

    ans = 1
    ans += (M-t)//x
    
    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, a)

if __name__ == '__main__':
    main()
