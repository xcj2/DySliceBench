#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]"):
    ret = [0] * N
    tmp = A[0]
    i = 1
    while i < N - i:
        tmp = A[i] + A[N - i] - tmp
        i += 1
    ret[N // 2 + 1] = tmp
    for i in range(N // 2, -1, -1):
        ret[i] = A[i] * 2 - ret[i + 1]
    for i in range(N // 2 + 2, N):
        ret[i] = A[i - 1] * 2 - ret[i - 1]
    print(' '.join([str(r) for r in ret]))
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
