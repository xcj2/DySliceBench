#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)
from pprint import pprint


def solve(N: int, A: "List[int]"):
    memo = [{} for _ in range(N + 1)]
    def rec(idx, rest, can_use=True):
        k = (rest, can_use)
        if rest * 2 >= N - idx + 2:
            return 0
        if rest == 0:
            return 0
        if k in memo[idx]:
            return memo[idx][k]

        ret = 0
        if not can_use:
            ret = rec(idx + 1, rest)
        elif rest * 2 > (N - idx):
            ret = A[idx] + rec(idx + 1, rest - 1, False)
        else:
            a = A[idx] + rec(idx + 1, rest - 1, False)
            b = rec(idx + 1, rest)
            ret = max(a, b)
        memo[idx][k] = ret
        return ret
    ret = rec(0, N // 2)
    print(ret)
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
