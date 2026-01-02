#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    if K!=0:
        ans = 0
        for j in range(K+1,N+1):      
            ans += (j-K) * (N//j)
            if N%j >=K:
                ans += N%j - K + 1
    else:
        ans = N * N

    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
