#!/usr/bin/env python3
import sys
import bisect

def solve(N: int, K: int, A: "List[int]", F: "List[int]"):
    import numpy as np

    A = np.array(A)
    F = np.array(F)

    A = np.sort(A)
    F = np.sort(F)[::-1]

    sum_A = A.sum()
    if sum_A <= K:
        ans = 0
    else:
        high = (A * F).max()
        low = 0
        mid = (high + low) // 2
        while low < mid < high:
            if sum_A - np.minimum(A, mid // F).sum() <= K: ##K回の修行いないで成し遂げれるなら
                high = mid
            else:
                low = mid
            mid = (high + low) // 2
        ans = high

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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    F = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A, F)

if __name__ == '__main__':
    main()
