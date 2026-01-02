#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

def solve(N: int, A: "List[int]"):
    counts = {}
    for a in A:
        if not a in counts:
            counts[a] = 0
        counts[a] += 1

    M = max(A)
    s = set(A)
    ret = 0
    used = [False] * (M + 1)
    for i in range(1, M + 1):
        if used[i]:
            continue
        if not i in s:
            continue
        if counts[i] == 1:
            ret += 1
        j = 1
        while i * j <= M:
            used[i * j] = True
            j += 1
    print(ret)


def _hoge(N, A):
    for i, v in enumerate(A):
        if used[i]:
            continue
        if not (i < N - 1 and v == A[i + 1]):
            ret += 1
        for j in range(i + 1, N):
            if A[j] % v == 0:
                used[j] = True
    print(ret)


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
