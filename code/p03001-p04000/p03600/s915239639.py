#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, A: "List[List[int]]"):
    es = [
        (A[i][j], i, j)
        for i in range(N)
        for j in range(i)
    ]
    es.sort(reverse=True)
    ans = 0
    for d, i, j in es:
        for k in range(N):
            if k == i or k == j:
                continue
            nd = A[i][k] + A[k][j]
            if nd < d:
                print(-1)
                return
            if nd == d:
                break
        else:
            ans += d
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A)


if __name__ == '__main__':
    main()
