#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    A.sort()

    if A[0] >= 0:
        ret = sum(A) - 2 * A[0]
        print(ret)
        tmp = A[0]
        for i in range(N - 2):
            print(tmp, A[i + 1])
            tmp -= A[i + 1]
        print(A[-1], tmp)

    elif A[-1] <= 0:
        ret = -sum(A[:-1]) + A[-1]
        print(ret)
        tmp = A[-1]
        for i in range(N - 1):
            idx = -1 - i - 1
            print(tmp, A[idx])
            tmp -= A[idx]

    else:
        ret = 0
        cnt = 0
        for a in A:
            if a < 0:
                ret += -a
                cnt += 1
            else:
                ret += a
        print(ret)
        idx = cnt - 1
        tmp = A[idx]
        for i in range(idx, N - 2):
            print(tmp, A[i + 1])
            tmp -= A[i + 1]
        tmp2 = A[-1]
        for i in range(0, cnt - 1):
            print(tmp2, A[i])
            tmp2 -= A[i]
        print(tmp2, tmp)
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
