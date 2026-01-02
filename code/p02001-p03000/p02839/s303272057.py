#!/usr/bin/env python3

import sys
from pprint import pprint
sys.setrecursionlimit(300000)


def solve(H: int, W: int, A: "List[List[int]]", B: "List[List[int]]"):
    diffs = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            diffs[i][j] = abs(A[i][j] - B[i][j])
    dp = [[[0] * 6401 for _ in range(W + 1)] for _ in range(H + 1)]
    dp[0][0][diffs[0][0]] += 1
    for i in range(H):
        for j in range(W):
            tmp = dp[i][j]
            for val, flg in enumerate(tmp):
                if not flg:
                    continue
                if val + diffs[i + 1][j] <= 6400:
                    dp[i + 1][j][abs(val + diffs[i + 1][j])] += 1
                if val + diffs[i][j + 1] <= 6400:
                    dp[i][j + 1][abs(val + diffs[i][j + 1])] += 1
                dp[i + 1][j][abs(val - diffs[i + 1][j])] += 1
                dp[i][j + 1][abs(val - diffs[i][j + 1])] += 1
                #dp[i + 1][j].add(abs(val + diffs[i + 1][j]))
                #dp[i + 1][j].add(abs(val - diffs[i + 1][j]))
                #dp[i][j + 1].add(abs(val + diffs[i][j + 1]))
                #dp[i][j + 1].add(abs(val - diffs[i][j + 1]))
    #ret = min(dp[H - 1][W - 1])
    ret = 0
    for val, flg in enumerate(dp[H - 1][W - 1]):
        if flg:
            ret = val
            break
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    B = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, A, B)

if __name__ == '__main__':
    main()
