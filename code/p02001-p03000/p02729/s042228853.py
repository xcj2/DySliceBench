#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int):
    import math
    def combination(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    ans = 0
    if N >= 2:
        ans += combination(N,2)
    if M >= 2:
        ans += combination(M,2)
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
    solve(N, M)

if __name__ == '__main__':
    main()
