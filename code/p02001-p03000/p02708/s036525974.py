#!/usr/bin/env python3
import sys
from itertools import accumulate

MOD = 1000000007  # type: int

def solve(N: int, K: int):
    a = list(range(0,N+1))

    left_a = list(accumulate(a))
    right_a = list(accumulate(a[::-1]))

    answer = 0
    for i in range(K,N+2):
        l = left_a[i-1]
        r = right_a[i-1]
        answer += r-l+1
        answer %= MOD
    
    print(answer)
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
