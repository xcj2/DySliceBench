#!/usr/bin/env python3
import sys
import numpy as np

MOD = 1000000007  # type: int

def solve(N: int, A: "List[int]"):
    mLEN = len(format(max(A),'b'))

    A = np.array(A)
    ans = 0
    d = 1
    while d < (1 << mLEN):
        cnt = np.count_nonzero(A & d)
        ans += (N - cnt) * cnt * d
        ans %= MOD
        d <<= 1
    print(ans)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
