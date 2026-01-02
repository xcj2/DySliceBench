#!/usr/bin/env python3

import sys, heapq, math
sys.setrecursionlimit(300000)


def solve(N: int, M: int, S: int, U: "List[int]", V: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    conns = [[] for _ in range(N)]
    for i in range(M):
        conns[U[i] - 1].append((V[i] - 1, A[i], B[i])) # cost, duration
        conns[V[i] - 1].append((U[i] - 1, A[i], B[i])) # cost, duration

    INF = float('inf')
    MAX_M = max(A) * N
    costs = [[None] * N for _ in range(N)]
    dp = [[INF] * (MAX_M + 1) for _ in range(N)]
    S = min(S, MAX_M)
    dp[0][S] = 0
    q = [(0, 0, S)] # time, idx, silver
    while q:
        t, i, m = heapq.heappop(q)
        if dp[i][m] < t:
            continue

        if m + C[i] <= MAX_M:
            if t + D[i] < dp[i][m + C[i]]:
                dp[i][m + C[i]] = t + D[i]
                heapq.heappush(q, (t + D[i], i, m + C[i]))

        for j, c, d in conns[i]:
            if m >= c:
                if t + d < dp[j][m - c]:
                    dp[j][m - c] = t + d
                    heapq.heappush(q, (t + d, j, m - c))

    for i in range(1, N):
        tmp = INF
        for v in dp[i]:
            tmp = min(tmp, v)
        print(tmp)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    U = [int()] * (M)  # type: "List[int]"
    V = [int()] * (M)  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (N)  # type: "List[int]"
    D = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, S, U, V, A, B, C, D)

if __name__ == '__main__':
    main()
