#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

from itertools import accumulate

def mod_factorial(n):
    value = 1
    for i in range(n,0,-1):
        value*=i
        value%=MOD
    return value

def solve(N: int, K: int, A: "List[int]"):
    A.sort()
    n = N-1
    r = K-1
    # nCkTable[i] = iCr
    nCkTable = [0]*(n+1)

    start = 1
    for _ in range(r):
        start *= n
        start %= MOD
        n -= 1

    bunbo = mod_factorial(r)
    bunbo_gyakugen = pow(bunbo,MOD-2,MOD)

    n = N-1
    for i in range(n, r-1, -1):
        nCkTable[i] = start*bunbo_gyakugen%MOD
        start*=pow(i,MOD-2,MOD)
        start*=i-r
        start%=MOD

    answer = 0
    for i in range(N):
        answer += A[i]*(nCkTable[i]-nCkTable[N-1-i])
        answer%=MOD
    print(answer%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
