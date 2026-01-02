import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**5)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


import numpy as np


def main():
    N, M = geta(int)
    A = np.array(list(geta(int)))
    A.sort()

    def c(x):
        """
        @return  # of handshake where hapiness >= x
        """
        X = np.searchsorted(A, x - A)
        return N * N - X.sum()

    left, right = 0, 2 * A[-1] + 1

    while left + 1 < right:
        middle = (left + right) // 2
        if c(middle) >= M:
            left = middle
        else:
            right = middle

    ans = 0
    Acum = np.zeros(N + 1, np.int64)
    Acum[:-1] = np.cumsum(A[::-1])[::-1]
    X = np.searchsorted(A, right - A)

    ans = Acum[X].sum() + (A * (N - X)).sum()

    ans += left * (M - (N * N - X.sum()))

    print(ans)


if __name__ == "__main__":
    main()