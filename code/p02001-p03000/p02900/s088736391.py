#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(A: int, B: int):
    def count(n):
        ret = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                ret += 1
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            ret += 1
        return ret
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    g = gcd(A, B)
    #print(g)
    ret = count(g)
    print(ret)
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
