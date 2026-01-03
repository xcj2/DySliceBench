#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, M_a: int, M_b: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    INF = float('inf')
    dp = [[INF] * 401 for _ in range(401)]
    dp[0][0] = 0
    for i in range(N):
        for x in range(400, -1, -1):
            for y in range(400, -1, -1):
                if dp[x][y] < INF:
                    dp[x + a[i]][y + b[i]] = min(dp[x + a[i]][y + b[i]], dp[x][y] + c[i])
    ret = INF
    for i in range(1, 401):
        for j in range(1, 401):
            if i % M_a == 0 and j % M_b == 0 and i // M_a == j // M_b:
                ret = min(ret, dp[i][j])
    if ret == INF:
        print(-1)
    else:
        print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M_a = int(next(tokens))  # type: int
    M_b = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]" 
    b = [int()] * (N)  # type: "List[int]" 
    c = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M_a, M_b, a, b, c)

if __name__ == '__main__':
    main()
