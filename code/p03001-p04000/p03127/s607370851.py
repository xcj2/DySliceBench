#!/usr/bin/env python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(N: int, A: "List[int]"):
    A.sort()
    ret = A[0]
    for i in range(1, N):
        if A[i] % ret > 0:
            ret = gcd(ret, A[i])
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
