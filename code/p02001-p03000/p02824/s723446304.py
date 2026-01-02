import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():

    N, M, V, P = geta(int)
    A = [-10**15] + list(geta(int))
    A.sort()

    target = A[N - P + 1]

    def c(x):
        """
        return True iff Problem x has chance to be chosen 
        """
        if x >= N - P + 1:
            return True

        v_left = M * max(V - x - P + 1, 0)

        Ax = A[x] + M
        if Ax < A[N - P + 1]:
            return False

        ok = False
        for i in range(x + 1, N - P + 1 + 1):
            ad = min(M, Ax - A[i])
            v_left -= ad
            if v_left <= 0:
                ok = True
                break

        return ok

    left, right = 0, N
    while left + 1 < right:
        middle = (left + right) // 2
        if c(middle):
            right = middle
        else:
            left = middle

    print(N - right + 1)


if __name__ == "__main__":
    main()