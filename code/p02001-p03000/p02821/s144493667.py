import sys
from collections import defaultdict
import bisect
import itertools
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**5)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N, M = geta(int)
    A = list(geta(int))
    A.sort()

    def c(x):
        """
        @return  # of handshake where hapiness >= x
        """
        ret = 0
        for a in A:
            ret += bisect.bisect_left(A, x - a)
        return N * N - ret

    left, right = 0, 2 * A[-1] + 1

    while left + 1 < right:
        middle = (left + right) // 2
        if c(middle) >= M:
            left = middle
        else:
            right = middle

    ans = 0
    Acum = list(itertools.accumulate(A[::-1]))[::-1]
    for a in A:
        idx = bisect.bisect_left(A, right - a)
        if idx < N:
            ans += Acum[idx] + a * (N - idx)
    ans += left * (M - c(right))

    print(ans)


if __name__ == "__main__":
    main()