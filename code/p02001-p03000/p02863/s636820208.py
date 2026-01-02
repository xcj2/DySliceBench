#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, T: int, A: "List[int]", B: "List[int]"):
    max_t = T + max(A)
    dp = [-1] * (max_t + 1)
    dp[0] = 0
    p = []
    for i in range(N):
        p.append((A[i], B[i]))
    p.sort()
    for i in range(N):
        for t in range(T - 1, -1, -1):
            if dp[t] >= 0:
                dp[t + p[i][0]] = max(dp[t + p[i][0]], dp[t] + p[i][1])
    ret = 0
    for v in dp:
        ret = max(ret, v)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, T, A, B)

if __name__ == '__main__':
    main()
